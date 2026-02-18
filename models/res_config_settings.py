# -*- coding: utf-8 -*-
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    color_0 = fields.Char(string='Color 0', config_parameter='colorlist_customizer.color_0')
    color_1 = fields.Char(string='Color 1', config_parameter='colorlist_customizer.color_1')
    color_2 = fields.Char(string='Color 2', config_parameter='colorlist_customizer.color_2')
    color_3 = fields.Char(string='Color 3', config_parameter='colorlist_customizer.color_3')
    color_4 = fields.Char(string='Color 4', config_parameter='colorlist_customizer.color_4')
    color_5 = fields.Char(string='Color 5', config_parameter='colorlist_customizer.color_5')
    color_6 = fields.Char(string='Color 6', config_parameter='colorlist_customizer.color_6')
    color_7 = fields.Char(string='Color 7', config_parameter='colorlist_customizer.color_7')
    color_8 = fields.Char(string='Color 8', config_parameter='colorlist_customizer.color_8')
    color_9 = fields.Char(string='Color 9', config_parameter='colorlist_customizer.color_9')
    color_10 = fields.Char(string='Color 10', config_parameter='colorlist_customizer.color_10')
    color_11 = fields.Char(string='Color 11', config_parameter='colorlist_customizer.color_11')
    
    # Opción para mostrar nombres de productos en mayúsculas
    product_names_uppercase = fields.Boolean(
        string='Nombres de productos en mayúsculas',
        config_parameter='colorlist_customizer.product_names_uppercase',
        default=False
    )
