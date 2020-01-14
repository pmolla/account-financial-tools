{
    "name": "Accounting Documents Management",
    "version": "12.0.1.0.0",
    "author": "Moldeo Interactive,ADHOC SA",
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": [
        "account",
        "base_validator",
    ],
    "data": [
        'view/account_journal_view.xml',
        'view/account_move_line_view.xml',
        'view/account_move_view.xml',
        'view/account_document_type_view.xml',
        'view/account_invoice_view.xml',
        'view/res_company_view.xml',
        'view/res_partner_view.xml',
        'view/report_invoice.xml',
        'view/account_chart_template_view.xml',
        'view/account_payment_view.xml',
        'view/account_payment_receiptbook_view.xml',
        'view/menuitem.xml',
        'view/account_portal_templates.xml',
        'report/invoice_report_view.xml',
        'data/account.document.type.csv',
        'data/mail_template_invoice.xml',
        'data/decimal_precision_data.xml',
        'wizards/account_invoice_refund_view.xml',
        'wizards/res_config_view.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
    ],
    "demo": [
    ],
    'images': [
    ],
    'installable': False,
    'post_init_hook': 'post_init_hook',
}
