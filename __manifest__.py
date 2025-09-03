# -*- coding: utf-8 -*-
{
    'name': "Precios Dinámicos en eCommerce (B2B)",
    'summary': """
        Muestra un precio de venta sugerido junto al precio de distribuidor
        en la página de producto del eCommerce.""",
    'description': """
        Este módulo mejora la experiencia de compra B2B en Odoo 16 Community.

        Características Principales:
        - Activa una vista de doble precio (Precio Sugerido vs. Precio de Cliente) configurable por sitio web.
        - Permite seleccionar la tarifa a usar como 'Precio Sugerido' desde los ajustes del sitio web.
        - Las etiquetas de los precios son dinámicas, mostrando el nombre de la tarifa correspondiente.
        - Utiliza el campo 'Compare at Price' del producto para mostrar ofertas (precios tachados) de forma manual y controlada.
        - Estilos dinámicos: el precio se muestra de forma prominente para usuarios públicos o cuando se selecciona la tarifa sugerida, y en una jerarquía visual clara para distribuidores.
        - Estilos gestionados por un archivo CSS externo para fácil mantenimiento y personalización.
    """,
    'author': "Marlon Macario",
    'website': "https://link-gt.com",
    'category': 'Website/eCommerce',
    'version': '16.0.1.1.0', 
    'license': 'LGPL-3',
    'depends': ['website_sale'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_sale_suggested_price/static/src/css/styles.css',
            'website_sale_suggested_price/static/src/js/margin_toggle.js', 
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}