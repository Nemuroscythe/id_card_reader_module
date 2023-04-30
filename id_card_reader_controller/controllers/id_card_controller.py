from odoo import http


class IdCardController(http.Controller):
    @http.route('/id_card_reader/test', type="json", auth='none', cors='*', method=['GET'])
    def test(self, **kw):
        return "Hello World"
