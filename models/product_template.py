# -*- coding: utf-8 -*-
from odoo import models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_suggested_price_info(self):
        """
        Calcula la información de precios completa (precio final, precio de lista, etc.)
        para la tarifa sugerida configurada en el sitio web.
        """
        self.ensure_one()
        website = self.env['website'].get_current_website()

        if not website.enable_dual_price or not website.suggested_pricelist_id:
            return False

        suggested_pricelist = website.suggested_pricelist_id
        
        # CORRECCIÓN: Usamos _get_combination_info() para obtener todos los detalles del precio,
        # incluyendo el precio de lista (para tachar) y el precio final.
        # Le pasamos forzosamente la tarifa que queremos usar.
        price_info = self._get_combination_info(pricelist=suggested_pricelist)
        
        # Añadimos el nombre de la tarifa al diccionario para usarlo en la plantilla.
        price_info['name'] = suggested_pricelist.name
        
        return price_info