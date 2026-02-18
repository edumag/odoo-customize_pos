# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request


class ColorlistCustomizerController(http.Controller):
    
    @http.route('/colorlist_customizer/config', type='http', auth='public', methods=['GET'])
    def get_config(self):
        """Devuelve la configuración del módulo como JSON"""
        params = request.env['ir.config_parameter'].sudo()
        
        # Obtener configuración de mayúsculas
        uppercase_value = params.get_param('colorlist_customizer.product_names_uppercase', 'False')
        
        config = {
            'product_names_uppercase': uppercase_value == 'True'
        }
        
        return request.make_response(
            json.dumps(config),
            headers=[('Content-Type', 'application/json')]
        )
