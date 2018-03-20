# -*- coding: utf-8 -*-
from odoo import http

# class Facture-prismacom(http.Controller):
#     @http.route('/facture-prismacom/facture-prismacom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/facture-prismacom/facture-prismacom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('facture-prismacom.listing', {
#             'root': '/facture-prismacom/facture-prismacom',
#             'objects': http.request.env['facture-prismacom.facture-prismacom'].search([]),
#         })

#     @http.route('/facture-prismacom/facture-prismacom/objects/<model("facture-prismacom.facture-prismacom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('facture-prismacom.object', {
#             'object': obj
#         })