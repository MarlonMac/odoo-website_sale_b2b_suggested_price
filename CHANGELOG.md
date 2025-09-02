# Changelog

Todas las notas de cambios de este proyecto se documentarán en este archivo.

## [1.0.0] - 2025-09-02

### Added
-   **Lanzamiento Inicial del Módulo**
-   Funcionalidad de doble precio (distribuidor vs. sugerido) en la página del producto.
-   Panel de configuración en los ajustes del Sitio Web para activar la función y seleccionar la tarifa de referencia.
-   Soporte para mostrar precios de oferta utilizando el campo `compare_list_price` del producto.
-   Estilos dinámicos que cambian la jerarquía visual del precio según el estado de sesión del usuario (público vs. logueado).
-   Inversión del orden de precios para mostrar el precio del distribuidor en la parte superior.
-   Lógica de estilo mejorada para usuarios con selector de tarifas.
-   Todos los estilos refactorizados a un archivo `styles.css` externo.