{
    'name': 'Construction Project Management',
    'version': '1.2',
    'category': 'Project',
    'author': 'Denyam Noguera',
    'summary': 'Gestion de proyectos de construccion',
    'depends': ['base', 'account', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/task_views.xml',
    ],
    'installable': True,
    'application': True,
    'icon': 'construction_project/static/description/icon.png',
}
