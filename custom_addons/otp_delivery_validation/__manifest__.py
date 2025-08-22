# -*- coding: utf-8 -*-
{
    'name': "OTP Delivery Validation",
    'summary': "Validate Cash on Delivery Orders with OTP",
    'description': """
        Adds OTP-based delivery validation to Sale Orders.
        - Generate OTP for customer when order is delivered
        - Customer provides OTP to delivery guy
        - Delivery guy enters OTP to validate delivery
    """,
    'author': "You",
    'website': "http://yourcompany.com",
    'category': 'Sales',
    'version': '1.0',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'demo/demo_data.xml',
        'views/delivery_validation_views.xml',
        'wizard/otp_verification_wizard.xml',
    ],
     'assets': {
        'web.assets_backend': [
            'otp_delivery_validation/static/src/css/styles.css',
        ],
     },
    'installable': True,
    'application': False,
    'auto_install': False,
}
