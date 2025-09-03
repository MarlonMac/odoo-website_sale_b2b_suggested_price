odoo.define('website_sale_suggested_price.margin_toggle', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.WebsiteSaleMarginToggle = publicWidget.Widget.extend({
    selector: '.o_wssp_margin_toggler',
    events: {
        'click': '_onClick',
    },

    /**
     * Al hacer clic, alterna la visibilidad de los elementos de margen.
     * @private
     * @param {Event} ev
     */
    _onClick: function (ev) {
        ev.preventDefault();
        const container = this.$el.closest('.o_wssp_margin_container');
        container.find('.o_wssp_margin_amount, .o_wssp_margin_percent').toggleClass('d-none');
    },
});

return publicWidget.registry.WebsiteSaleMarginToggle;

});