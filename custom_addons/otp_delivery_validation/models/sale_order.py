# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    otp_code = fields.Char("OTP Code", readonly=True)
    otp_verified = fields.Boolean("OTP Verified", default=False)

    def generate_otp(self):
        """Generate a random 6-digit OTP and store it."""
        otp = str(random.randint(100000, 999999))
        self.write({'otp_code': otp, 'otp_verified': False})
        _logger.info(f"OTP for {self.partner_id.name}: {otp}")  # TODO: integrate SMS/Email
        return True

    def action_open_otp_verification(self):
        """Open wizard to verify OTP."""
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'otp.verification.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_sale_order_id': self.id},
        }
