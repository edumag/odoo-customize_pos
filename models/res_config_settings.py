# -*- coding: utf-8 -*-
from odoo import models, fields

# Colores por defecto para las categorías del TPV
DEFAULT_COLORS = [
    "#f15b40",
    "#ffdd00",
    "#af7e6c",
    "#f7941d",
    "#00bfdf",
    "#8dc63f",
    "#f173ac",
    "#ee3f75",
    "#b58f2e",
    "#FF00FF",
    "#b3b6e7",
    "#b3b62a",
]


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    color_0 = fields.Char(
        string="Color 0",
        config_parameter="customize_pos.color_0",
        default=DEFAULT_COLORS[0],
    )
    color_1 = fields.Char(
        string="Color 1",
        config_parameter="customize_pos.color_1",
        default=DEFAULT_COLORS[1],
    )
    color_2 = fields.Char(
        string="Color 2",
        config_parameter="customize_pos.color_2",
        default=DEFAULT_COLORS[2],
    )
    color_3 = fields.Char(
        string="Color 3",
        config_parameter="customize_pos.color_3",
        default=DEFAULT_COLORS[3],
    )
    color_4 = fields.Char(
        string="Color 4",
        config_parameter="customize_pos.color_4",
        default=DEFAULT_COLORS[4],
    )
    color_5 = fields.Char(
        string="Color 5",
        config_parameter="customize_pos.color_5",
        default=DEFAULT_COLORS[5],
    )
    color_6 = fields.Char(
        string="Color 6",
        config_parameter="customize_pos.color_6",
        default=DEFAULT_COLORS[6],
    )
    color_7 = fields.Char(
        string="Color 7",
        config_parameter="customize_pos.color_7",
        default=DEFAULT_COLORS[7],
    )
    color_8 = fields.Char(
        string="Color 8",
        config_parameter="customize_pos.color_8",
        default=DEFAULT_COLORS[8],
    )
    color_9 = fields.Char(
        string="Color 9",
        config_parameter="customize_pos.color_9",
        default=DEFAULT_COLORS[9],
    )
    color_10 = fields.Char(
        string="Color 10",
        config_parameter="customize_pos.color_10",
        default=DEFAULT_COLORS[10],
    )
    color_11 = fields.Char(
        string="Color 11",
        config_parameter="customize_pos.color_11",
        default=DEFAULT_COLORS[11],
    )

    # Opción para mostrar nombres de productos en mayúsculas
    product_names_uppercase = fields.Boolean(
        string="Nombres de productos en mayúsculas",
        config_parameter="customize_pos.product_names_uppercase",
        default=False,
    )

    # Opción para mostrar nombres de categorías en mayúsculas
    category_names_uppercase = fields.Boolean(
        string="Nombres de categorías en mayúsculas",
        config_parameter="customize_pos.category_names_uppercase",
        default=False,
    )
