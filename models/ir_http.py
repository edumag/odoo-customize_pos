# -*- coding: utf-8 -*-
from odoo import models


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()

        params = self.env['ir.config_parameter'].sudo()
        colors = {}
        defaults = [
            '#f15b40', '#ffdd00', '#af7e6c', '#f7941d',
            '#00bfdf', '#8dc63f', '#f173ac', '#ee3f75',
            '#b58f2e', '#FF00FF', '#b3b6e7', '#b3b62a'
        ]

        for i in range(12):
            colors[f'colorlist_{i}'] = params.get_param(
                f'customize_pos.color_{i}', defaults[i]
            )

        result['customize_pos'] = colors

        # Añadir configuración de nombres de productos en mayúsculas
        product_uppercase = params.get_param('customize_pos.product_names_uppercase', 'False')
        result['customize_pos_product_uppercase'] = product_uppercase == 'True'

        # Añadir configuración de nombres de categorías en mayúsculas
        category_uppercase = params.get_param('customize_pos.category_names_uppercase', 'False')
        result['customize_pos_category_uppercase'] = category_uppercase == 'True'

        return result
