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
   
     # --- NUEVOS CAMPOS ---
    show_margin = fields.Boolean(
        string="Mostrar Margen de Ahorro",
        help="Activa esta opción para mostrar el ahorro del distribuidor (diferencia entre precio sugerido y su precio)."
    )
    margin_display_type = fields.Selection(
        [('percentage', 'Porcentaje'), ('absolute', 'Monto Absoluto')],
        string="Formato de Margen Predeterminado",
        default='percentage',
        help="Selecciona el formato por defecto para mostrar el margen de ahorro."
    )
    allow_user_margin_type_change = fields.Boolean(
        string="Permitir Cambiar Formato",
        help="Permite a los usuarios distribuidores cambiar entre la vista de porcentaje y monto absoluto en la página del producto."
    )