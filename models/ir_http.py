# -*- coding: utf-8 -*-
from odoo import models


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()
        
        params = self.env['ir.config_parameter'].sudo()
        colors = {}
        defaults = [
            '#FF0000', '#FF7F00', '#FFFF00', '#00FF00',
            '#0000FF', '#4B0082', '#9400D3', '#FF1493',
            '#00FFFF', '#FF00FF', '#808080', '#000000'
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
