{
    'name': 'Gestion de Contrats',
    'version': '1.0',
    'summary': 'Module pour la gestion des contrats et la facturation',
    'sequence': 10,
    'description': "Gérer les contrats et générer des factures",
    'category': 'Accounting',
    'author': 'Mikalo FItia RAMIANDRISON',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/contract_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}