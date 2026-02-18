# -*- coding: utf-8 -*-
{
    'name': 'Colorlist Customizer',
    'version': '18.0.1.0.9',
    'category': 'Technical',
    'summary': 'Personaliza los colores del widget colorlist',
    'description': """
        Permite al administrador personalizar los 12 colores del widget
        o_colorlist desde los Ajustes de Odoo.
    """,
    'author': 'Eduardo Magrané',
    'website': 'https://lesolivex.com',
    'license': 'LGPL-3',
    'depends': ['web', 'point_of_sale'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/pos_assets.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'colorlist_customizer/static/src/scss/colorlist_customizer.scss',
            'colorlist_customizer/static/src/js/colorlist_patch.js',
        ],
        'point_of_sale.assets': [
            'colorlist_customizer/static/src/scss/colorlist_customizer.css',
            'colorlist_customizer/static/src/js/colorlist_patch.js',
            'colorlist_customizer/static/src/js/pos_category_button.js',
            'colorlist_customizer/static/src/xml/pos_category_button.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
