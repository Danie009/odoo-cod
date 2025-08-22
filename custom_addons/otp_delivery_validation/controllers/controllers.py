# -*- coding: utf-8 -*-
# from odoo import http


# class OtpDeliveryValidation(http.Controller):
#     @http.route('/otp_delivery_validation/otp_delivery_validation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/otp_delivery_validation/otp_delivery_validation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('otp_delivery_validation.listing', {
#             'root': '/otp_delivery_validation/otp_delivery_validation',
#             'objects': http.request.env['otp_delivery_validation.otp_delivery_validation'].search([]),
#         })

#     @http.route('/otp_delivery_validation/otp_delivery_validation/objects/<model("otp_delivery_validation.otp_delivery_validation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('otp_delivery_validation.object', {
#             'object': obj
#         })

