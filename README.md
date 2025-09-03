# Precios Dinámicos en eCommerce (B2B) para Odoo 16

Este módulo mejora la experiencia de compra B2B en Odoo 16 Community Edition, permitiendo mostrar un precio de venta al público sugerido junto al precio específico del distribuidor en la página del producto.

## Características Principales ✨

* **Vista de Doble Precio**: Muestra simultáneamente el precio de distribuidor y el precio de venta sugerido, creando una clara jerarquía visual.
* **Cálculo de Margen de Ahorro**: Muestra automáticamente el ahorro del distribuidor (configurable para ser en monto absoluto o porcentaje) para reforzar el valor de la compra B2B.
* **Totalmente Configurable**: Activa o desactiva la funcionalidad por sitio web y selecciona qué tarifa usar como "Precio Sugerido" directamente desde los Ajustes del Sitio Web.
* **Control Manual de Ofertas**: Utiliza el campo nativo de Odoo **"Compare at Price"** en la ficha del producto para mostrar un precio tachado, dándote control total sobre las ofertas.
* **Estilos Dinámicos**:
    * Para **usuarios públicos** o cuando se selecciona la tarifa de venta sugerida, el precio se muestra de forma prominente.
    * Para **distribuidores**, su precio aparece como el principal (grande, arriba) y el sugerido como referencia secundaria (pequeño, abajo).
* **Etiquetas Dinámicas**: Las etiquetas de los precios ("Dist. VIP", "Precio Sugerido de Venta", etc.) se toman directamente del nombre de la tarifa.
* **CSS Centralizado**: Todos los estilos están en un archivo CSS dedicado, facilitando la personalización y el mantenimiento.

## Configuración ⚙️

1.  Instala el módulo.
2.  Navega a **Sitio Web > Configuración > Ajustes**.
3.  Asegúrate de tener seleccionado el sitio web correcto.
4.  Busca la sección **Vista de Doble Precio (B2B)**.
5.  ✅ Activa la casilla **"Activar Vista de Doble Precio"**.
6.  👇 En el campo **"Tarifa de Precio Sugerido"**, selecciona la lista de precios que actuará como precio de referencia para el público (ej. "Precio Sugerido de Venta").
7.  ✅ Opcionalmente, activa **"Calcular Margen de Ahorro"** para mostrar la diferencia entre el precio sugerido y el del distribuidor.
    * Puedes elegir el **formato predeterminado** (Porcentaje o Monto Absoluto).
    * Puedes permitir que el usuario cambie el formato de visualización en la página del producto.
8.  Guarda los cambios.

## Uso 🚀

* **Para mostrar una oferta (precio tachado)**: Edita un producto, ve a la pestaña "Ventas" y establece un valor en el campo **"Compare at Price"**. Este valor se mostrará tachado.
* **Para Vendedores**: Si un usuario tiene permiso para cambiar de tarifa en el sitio web, al seleccionar la "Tarifa de Precio Sugerido", verá el precio en el formato prominente principal.

## Autor

* Marlon Macario
* Website: https://link-gt.com