{
    'name': 'Auth Signup Form',
    'version': '13.0.1.0.0',
    'category': 'Website',
    'summary': 'Auth signup form with extra fields',
    'description': """
        This module add phone number, address and birth date to auth sign up page
        * Phone Number
        * Address
        * Birth date
    """,
    'sequence': 1,
    'author': 'Futurelens',
    'website': 'http://thefuturelens.com',
    'depends': ['auth_signup'],
    'data': [
        'views/auth_signup_extend_views.xml',
        'views/res_partner_view.xml',
    ],
    'images': [
        'static/description/auth_signup_banner.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
