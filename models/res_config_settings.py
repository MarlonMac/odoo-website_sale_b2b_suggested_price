# -*- coding: utf-8 -*-
from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Campos relacionados para exponer la configuración del sitio web en los Ajustes Generales
    website_enable_dual_price = fields.Boolean(
        related='website_id.enable_dual_price',
        readonly=False
    )
    website_suggested_pricelist_id = fields.Many2one(
        related='website_id.suggested_pricelist_id',
        readonly=False
    )