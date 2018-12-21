# -*- coding: utf-8 -*-
{
    'name': 'Quick Task',
    'version': '11.0.1.0.0',
    'category': 'Project',
    'summary': 'Create Quick Task for Project',
    'description': """
        This module allow to create quick task for project
    """,
    'sequence': 1,
    'author': 'Futurelens',
    'website': 'http://thefuturelens.com',
    'depends': ['base', 'project'],
    'data': [
        'views/project_view.xml',
    ],
    'qweb': [],
    'css': [],
    'js': [],
    'images': [
        'static/description/quick_task_banner.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
