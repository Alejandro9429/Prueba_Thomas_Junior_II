from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    spotify_client_id = fields.Char(
        string='Spotify Client ID',
        config_parameter='spotify_partner.client_id')
    spotify_client_secret = fields.Char(
        string='Spotify Client Secret',
        config_parameter='spotify_partner.client_secret')