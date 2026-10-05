from odoo import fields, models


class SpotifyTrack(models.Model):
    _name = 'spotify.track'
    _description = 'Recommended Track'

    partner_id = fields.Many2one(
        'res.partner', string='Customer', required=True, ondelete='cascade')
    genre_id = fields.Many2one(
        'spotify.genre', string='Genre', ondelete='set null')
    name = fields.Char(string='Track')
    artist = fields.Char(string='Artist')
    album = fields.Char(string='Album')
    spotify_id = fields.Char(string='Spotify ID')
    url = fields.Char(string='URL', required=True)