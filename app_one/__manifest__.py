{
    'name': 'App One',
    'author': 'abdo fared',
    'version': '17.0.0.1.0',
    'depends': ['base','sale_management','account','mail','contacts'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/data.xml',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml',
        'views/res_partner_view.xml',
        'views/building_view.xml',
        'views/property_history_view.xml',
        'views/sale_order_line.xml',
        'views/account_move_view.xml',
        'wizard/change_state_wizard.xml',
        'reports/property_report.xml',
        'reports/sale_order_line_report.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'app_one/static/src/css/property.css',

            # ضيف الملفات الـ OWL بالطريقة الصحيحة
            'app_one/static/src/components/listView/listView.xml',
            'app_one/static/src/components/listView/listView.js',
            'app_one/static/src/components/listView/listView.css',
        ],
    },

    'qweb': [
        'app_one/static/src/components/listView/listView.xml',
    ],

    'application': True
}

# {


#     'name': 'App One',
#     'author': 'abdo fared',
#     'category':'',
#     'version':'17.0.0.1.0',
#     'depends':['base','sale_management','account', 'mail','contacts'],
#     'data':[
#         'security/security.xml',
#         'security/ir.model.access.csv',
#         'data/sequence.xml',
#         'views/base_menu.xml',
#         'views/property_view.xml',
#         'views/owner_view.xml',
#         'views/tag_view.xml',
#         'views/sale_order_view.xml',
#         'views/res_partner_view.xml',
#         'views/building_view.xml',
#         'views/property_history_view.xml',
#         'views/sale_order_line.xml',
#         'views/account_move_view.xml',
#         'wizard/change_state_wizard.xml',
#         'reports/property_report.xml',
#         'reports/sale_order_line_report.xml',
#     ],
#     'assets': {
#         'web.assets_backend': [
#            'app_one/static/src/css/property.css',
#            'app_one/static/src/components/listView/listView.css',
#            'app_one/static/src/components/listView/listView.js',
#            'app_one/static/src/components/listView/listView.xml',
#         ],
#         'web.report_assets_common': [
#             'app_one/static/src/css/font.css',

#         ],
        
#     },
#     'qweb': [
#         'app_one/static/src/components/listView/listView.xml',
#     ],

#     'application':'true'
#     }


