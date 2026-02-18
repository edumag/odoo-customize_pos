# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request


class CustomizePosController(http.Controller):
    
    @http.route('/customize_pos/config', type='http', auth='public', methods=['GET'])
    def get_config(self):
        """Devuelve la configuración del módulo como JSON"""
        params = request.env['ir.config_parameter'].sudo()
        
        # Obtener configuraciones
        product_uppercase = params.get_param('customize_pos.product_names_uppercase', 'False')
        category_uppercase = params.get_param('customize_pos.category_names_uppercase', 'False')
        
        config = {
            'product_names_uppercase': product_uppercase == 'True',
            'category_names_uppercase': category_uppercase == 'True'
        }
        
        return request.make_response(
            json.dumps(config),
            headers=[('Content-Type', 'application/json')]
        )
