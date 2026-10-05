import base64
import logging
import random

import requests

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

TOKEN_URL = 'https://accounts.spotify.com/api/token'
SEARCH_URL = 'https://api.spotify.com/v1/search'
REQUEST_TIMEOUT = 10
PAGE_SIZE = 10
MAX_OFFSET = 990


class ResPartner(models.Model):
    _inherit = 'res.partner'

    spotify_genre_ids = fields.Many2many(
        'spotify.genre', string='Music Genres')
    spotify_track_ids = fields.One2many(
        'spotify.track', 'partner_id', string='Recommended Tracks')

    @api.model_create_multi
    def create(self, vals_list):
        partners = super().create(vals_list)
        partners.filtered('spotify_genre_ids')._update_spotify_recommendations()
        return partners

    def write(self, vals):
        result = super().write(vals)
        if 'spotify_genre_ids' in vals:
            self._update_spotify_recommendations()
        return result

    def _update_spotify_recommendations(self):
        token = self._get_spotify_token()
        if not token:
            return
        track_model = self.env['spotify.track']
        for partner in self:
            new_tracks = []
            for genre in partner.spotify_genre_ids:
                track_data = self._get_spotify_random_track(token, genre.name)
                if track_data:
                    track_data.update(
                        partner_id=partner.id, genre_id=genre.id)
                    new_tracks.append(track_data)
            partner.spotify_track_ids.unlink()
            if new_tracks:
                track_model.create(new_tracks)

    @api.model
    def _get_spotify_token(self):
        params = self.env['ir.config_parameter'].sudo()
        client_id = params.get_param('spotify_partner.client_id')
        client_secret = params.get_param('spotify_partner.client_secret')
        if not client_id or not client_secret:
            _logger.warning('Spotify: credentials are missing in Settings.')
            return None

        credentials = base64.b64encode(
            f'{client_id}:{client_secret}'.encode()).decode()
        try:
            response = requests.post(
                TOKEN_URL,
                headers={'Authorization': f'Basic {credentials}'},
                data={'grant_type': 'client_credentials'},
                timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            return response.json()['access_token']
        except (requests.RequestException, KeyError, ValueError) as error:
            _logger.warning('Spotify: could not get a token: %s', error)
            return None

    @api.model
    def _get_spotify_random_track(self, token, genre_name):
        headers = {'Authorization': f'Bearer {token}'}
        query = 'genre:"%s"' % genre_name.replace('"', '')

        for offset in (random.randint(0, MAX_OFFSET), 0):
            try:
                response = requests.get(
                    SEARCH_URL,
                    headers=headers,
                    params={'q': query, 'type': 'track',
                            'limit': PAGE_SIZE, 'offset': offset},
                    timeout=REQUEST_TIMEOUT)
                response.raise_for_status()
                items = response.json().get('tracks', {}).get('items', [])
            except (requests.RequestException, ValueError) as error:
                _logger.warning(
                    'Spotify: search failed for "%s": %s', genre_name, error)
                continue

            items = [item for item in items if item]
            if items:
                item = random.choice(items)
                return {
                    'name': item.get('name'),
                    'artist': ', '.join(
                        artist['name'] for artist in item.get('artists', [])),
                    'album': (item.get('album') or {}).get('name'),
                    'spotify_id': item.get('id'),
                    'url': item['external_urls']['spotify'],
                }
        return None