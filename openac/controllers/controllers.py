# -*- coding: utf-8 -*-
# from odoo import http


# class Openac(http.Controller):
#     @http.route('/openac/openac', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openac/openac/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('openac.listing', {
#             'root': '/openac/openac',
#             'objects': http.request.env['openac.openac'].search([]),
#         })

#     @http.route('/openac/openac/objects/<model("openac.openac"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openac.object', {
#             'object': obj
#         })
