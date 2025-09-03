# Changelog

Todas las notas de cambios de este proyecto se documentarán en este archivo.

## [1.1.0] - 2025-09-03

### Added
-   **[CARACTERÍSTICA]** Se agregó una opción en los ajustes del sitio web para mostrar el margen de ahorro del distribuidor.
-   La visualización del margen se puede configurar para mostrarse como un monto absoluto o un porcentaje.
-   Se añadió una opción para permitir (o no) que el usuario final cambie el modo de visualización del margen en la página del producto.
-   Nuevas traducciones en la vista de configuración para las nuevas opciones.

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