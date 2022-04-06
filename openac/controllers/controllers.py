# -*- coding: utf-8 -*-
from odoo import http


class Openac(http.Controller):
     @http.route('/openac/openac', auth='public', website=True)
     def index(self, **kw):
        Teachers = http.request.env['openac.teachers']
        return http.request.render('openac.index', {
            'teachers':  Teachers.search([]),
        })

     @http.route('/openac/<name>/', auth='public', website=True)
     def teacher(self, name):
         return '<h1>{}</h1>'.format(name)

     @http.route('/openac/<int:id>/', auth='public', website=True)
     def teacher(self, id):
         return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

     @http.route('/openac/<model("openac.teachers"):teacher>/', auth='public', website=True)
     def teacher(self, teacher):
         return http.request.render('openac.biography', {
             'person': teacher
         })
'''
     @http.route('/openac/openac/objects', auth='public')
     def list(self, **kw):
         return http.request.render('openac.listing', {
             'root': '/openac/openac',
             'objects': http.request.env['openac.openac'].search([]),
         })

     @http.route('/openac/openac/objects/<model("openac.openac"):obj>', auth='public')
     def object(self, obj, **kw):
         return http.request.render('openac.object', {
             'object': obj
         })
'''
