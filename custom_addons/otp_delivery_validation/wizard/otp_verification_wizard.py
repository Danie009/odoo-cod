# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class OTPVerificationWizard(models.TransientModel):
    _name = 'otp.verification.wizard'
    _description = 'OTP Verification Wizard'

    sale_order_id = fields.Many2one('sale.order', string="Sale Order", required=True, readonly=True)
    entered_otp = fields.Char("Enter OTP", required=True)

    def action_verify_otp(self):
        """Verify OTP entered by delivery person."""
        if self.entered_otp == self.sale_order_id.otp_code:
            self.sale_order_id.write({'otp_verified': True})
        else:
            raise UserError("Invalid OTP. Please try again.")
