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
                f'colorlist_customizer.color_{i}', defaults[i]
            )
        
        result['colorlist_customizer'] = colors
        
        # Añadir configuración de nombres de productos en mayúsculas
        uppercase_value = params.get_param('colorlist_customizer.product_names_uppercase', 'False')
        result['colorlist_customizer_product_uppercase'] = uppercase_value == 'True'
        
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info('ColorlistCustomizer: product_names_uppercase = %s', result['colorlist_customizer_product_uppercase'])
        
        return result
