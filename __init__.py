# -*- coding: utf-8 -*-
from . import models
from . import controllers

from odoo import api, SUPERUSER_ID


def _set_default_colors(cr, registry):
    """Set default colors in ir.config_parameter when module is installed"""
    env = api.Environment(cr, SUPERUSER_ID, {})

    defaults = [
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

    params = env["ir.config_parameter"].sudo()

    for i in range(12):
        param_name = f"customize_pos.color_{i}"
        # Only set if not already exists
        existing = params.get_param(param_name)
        if not existing:
            params.set_param(param_name, defaults[i])
            print(f"[CustomizePOS] Set default color {i}: {defaults[i]}")
