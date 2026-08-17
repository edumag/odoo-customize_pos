# -*- coding: utf-8 -*-
{
    "name": "Customize POS (TPV)",
    "version": "18.0.1.0.28",
    "category": "Technical",
    "summary": "Personalización visual del TPV (categorías, colores, textos)",
    "description": """Personaliza el TPV: colores de categorías, nombres de productos y categorías en mayúsculas, y más opciones visuales desde los ajustes.""",
    "author": "Eduardo Magrané",
    "website": "https://lesolivex.com",
    "license": "LGPL-3",
    "depends": ["web", "point_of_sale"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/backend_assets.xml",
        "views/pos_assets.xml",
    ],
    "assets": {
        "web.assets_backend": [
            'customize_pos/static/src/scss/general_backend_styles.scss',
            # CSS con variables de fallback (se sobrescribe con CSS dinámico inline)
            "customize_pos/static/src/scss/colorlist_variables.css",
            "customize_pos/static/src/scss/colorlist_customizer.css",
            "customize_pos/static/src/js/colorlist_patch.js",
        ],
        "point_of_sale.assets": [
            # Los archivos CSS ahora se cargan directamente en el template pos_assets.xml
            "customize_pos/static/src/xml/pos_category_button.xml",
            "customize_pos/static/src/js/colorlist_patch.js",
            "customize_pos/static/src/js/pos_product_names.js",
        ],
        'web.assets_frontend': [
            'customize_pos/static/src/scss/general_frontend_styles.scss'
        ]
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
