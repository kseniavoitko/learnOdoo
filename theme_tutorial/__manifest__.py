# -*- coding: utf-8 -*-
{
    'name': 'Theme tutorial',
    'description': 'My theme tutorial.',
    'version': '1.0',
    'author': 'Ksenia',
    'category': 'Theme/Creative',

    'depends': ['website', 'website'],
    'data': [
        'views/layout.xml',
        'views/pages.xml',
        'views/snippets.xml',
        'views/options.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_tutorial/static/scss/style.scss',
        ],
        'web._assets_primary_variables': [
            'theme_tutorial/static/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            'theme_tutorial/static/src/scss/bootstrap_overridden.scss',
        ],
        'website.assets_editor': [
            'theme_tutorial/static/src/js/tutorial_editor.js',
        ],
    }
}
