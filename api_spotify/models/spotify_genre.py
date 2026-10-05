from odoo import fields, models


class SpotifyGenre(models.Model):
    _name = 'spotify.genre'
    _description = 'Music Genre'

    name = fields.Char(string='Genre', required=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'This genre already exists.'),
    ]