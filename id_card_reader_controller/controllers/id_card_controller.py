from odoo import http


class IdCardController(http.Controller):
    @http.route('/id_card_reader/test', type="json", auth='none', cors='*', method=['POST'])
    def test(self, **kw):
        return "Hello World"
