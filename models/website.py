# -*- coding: utf-8 -*-
from odoo import fields, models

class Website(models.Model):
    _inherit = 'website'

    enable_dual_price = fields.Boolean(
        string="Activar Vista de Doble Precio",
        help="Muestra el precio sugerido junto al precio del cliente en la página del producto."
    )
    suggested_pricelist_id = fields.Many2one(
        comodel_name='product.pricelist',
        string="Tarifa de Precio Sugerido",
        help="Seleccione la tarifa que se usará como 'Precio Sugerido de Venta'."
    )