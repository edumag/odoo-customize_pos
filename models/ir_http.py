# -*- coding: utf-8 -*-
import logging
from odoo import models
from odoo.http import request

_logger = logging.getLogger(__name__)


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        result = super(IrHttp, self).session_info()

        # Asegurar que tenemos un environment válido
        if not self.env:
            _logger.warning("[CustomizePOS] No environment in session_info")
            return result

        try:
            params = self.env["ir.config_parameter"].sudo()
            colors = {}
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

            for i in range(12):
                param_value = params.get_param(f"customize_pos.color_{i}")
                # Si no existe el parámetro, usar el valor por defecto
                if param_value:
                    colors[f"colorlist_{i}"] = param_value
                else:
                    colors[f"colorlist_{i}"] = defaults[i]

            result["customize_pos"] = colors
            _logger.info("[CustomizePOS] Colors added to session_info: %s", colors)

            # Añadir configuración de nombres de productos en mayúsculas
            product_uppercase = params.get_param(
                "customize_pos.product_names_uppercase", "False"
            )
            result["customize_pos_product_uppercase"] = product_uppercase == "True"

            # Añadir configuración de nombres de categorías en mayúsculas
            category_uppercase = params.get_param(
                "customize_pos.category_names_uppercase", "False"
            )
            result["customize_pos_category_uppercase"] = category_uppercase == "True"
        except Exception as e:
            _logger.error("[CustomizePOS] Error in session_info: %s", str(e))

        return result
