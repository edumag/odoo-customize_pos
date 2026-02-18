# -*- coding: utf-8 -*-
{
    'name': 'Colorlist Customizer',
    'version': '18.0.1.0.25',
    'category': 'Technical',
    'summary': 'Personaliza colores y visualización del TPV',
    'description': """Permite al administrador personalizar los 12 colores del widget o_colorlist y las opciones de visualización del TPV desde los Ajustes de Odoo.""",
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
            'colorlist_customizer/static/src/scss/pos_product_names.css',
            'colorlist_customizer/static/src/js/colorlist_patch.js',
            'colorlist_customizer/static/src/xml/pos_category_button.xml',
            'colorlist_customizer/static/src/js/pos_product_names.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
