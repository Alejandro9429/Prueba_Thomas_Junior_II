{
    'name': 'Spotify Partner',
    'version': '14.0.1.0.0',
    'summary': 'Recommends Spotify tracks based on the genres of a customer',
    'category': 'Contacts',
    'author': 'Alejandro',
    'depends': ['base', 'base_setup', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}