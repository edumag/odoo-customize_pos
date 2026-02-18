# -*- coding: utf-8 -*-
{
    'name': 'Customize POS (TPV)',
    'version': '18.0.1.0.27',
    'category': 'Technical',
    'summary': 'Personalización visual del TPV (categorías, colores, textos)',
    'description': """Personaliza el TPV: colores de categorías, nombres de productos y categorías en mayúsculas, y más opciones visuales desde los ajustes.""",
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
            'customize_pos/static/src/scss/colorlist_customizer.scss',
            'customize_pos/static/src/js/colorlist_patch.js',
        ],
        'point_of_sale.assets': [
            'customize_pos/static/src/scss/colorlist_customizer.css',
            'customize_pos/static/src/scss/pos_product_names.css',
            'customize_pos/static/src/js/colorlist_patch.js',
            'customize_pos/static/src/xml/pos_category_button.xml',
            'customize_pos/static/src/js/pos_product_names.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
