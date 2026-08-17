# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request


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


class CustomizePosController(http.Controller):
    @http.route("/customize_pos/config", type="http", auth="public", methods=["GET"])
    def get_config(self):
        """Devuelve la configuración del módulo como JSON"""
        params = request.env["ir.config_parameter"].sudo()

        # Obtener configuraciones
        product_uppercase = params.get_param(
            "customize_pos.product_names_uppercase", "False"
        )
        category_uppercase = params.get_param(
            "customize_pos.category_names_uppercase", "False"
        )

        config = {
            "product_names_uppercase": product_uppercase == "True",
            "category_names_uppercase": category_uppercase == "True",
        }

        return request.make_response(
            json.dumps(config), headers=[("Content-Type", "application/json")]
        )

    @http.route(
        "/customize_pos/colors.css", type="http", auth="public", methods=["GET"]
    )
    def get_colors_css(self):
        """Devuelve el CSS con los colores personalizados"""
        params = request.env["ir.config_parameter"].sudo()

        # Obtener colores personalizados o usar valores por defecto
        colors = []
        for i in range(12):
            color = params.get_param(f"customize_pos.color_{i}", DEFAULT_COLORS[i])
            colors.append(color)

        # Generar CSS con las variables
        css_content = f"""/* Variables CSS para colores personalizados - Generado dinámicamente */
:root {{
  --colorlist-color-0: {colors[0]};
  --colorlist-color-1: {colors[1]};
  --colorlist-color-2: {colors[2]};
  --colorlist-color-3: {colors[3]};
  --colorlist-color-4: {colors[4]};
  --colorlist-color-5: {colors[5]};
  --colorlist-color-6: {colors[6]};
  --colorlist-color-7: {colors[7]};
  --colorlist-color-8: {colors[8]};
  --colorlist-color-9: {colors[9]};
  --colorlist-color-10: {colors[10]};
  --colorlist-color-11: {colors[11]};
}}
"""

        return request.make_response(
            css_content, headers=[("Content-Type", "text/css")]
        )

    @http.route("/customize_pos/debug", type="http", auth="public", methods=["GET"])
    def debug_colors(self):
        """Debug endpoint para verificar los colores guardados"""
        params = request.env["ir.config_parameter"].sudo()

        result = {"colors": {}, "message": "Debug info for customize_pos colors"}

        for i in range(12):
            param_name = f"customize_pos.color_{i}"
            value = params.get_param(param_name)
            result["colors"][f"color_{i}"] = {
                "param_name": param_name,
                "value": value,
                "exists": value is not None,
            }

        return request.make_response(
            json.dumps(result, indent=2), headers=[("Content-Type", "application/json")]
        )
