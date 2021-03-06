# This is your project's main settings file that can be committed to your
# repo. If you need to override a setting locally, use settings_local.py

from funfactory.settings_base import *

# Name of the top-level module where you put all your apps.
# If you did not install Playdoh with the funfactory installer script
# you may need to edit this value. See the docs about installing from a
# clone.
PROJECT_MODULE = 'mozldap'

MIDDLEWARE_CLASSES = (
  # deliberately empty
)

# Defines the views served for root URLs.
ROOT_URLCONF = '%s.urls' % PROJECT_MODULE

INSTALLED_APPS = (
    # Application base, containing global templates.
    '%s.base' % PROJECT_MODULE,
    '%s.docs' % PROJECT_MODULE,
)

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'docs',
]

# BrowserID configuration
#AUTHENTICATION_BACKENDS = [
#    'django_browserid.auth.BrowserIDBackend',
#    'django.contrib.auth.backends.ModelBackend',
#]

#SITE_URL = 'http://127.0.0.1:8000'
#LOGIN_URL = '/'
#LOGIN_REDIRECT_URL = 'examples.home'
#LOGIN_REDIRECT_URL_FAILURE = 'examples.home'

#TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS) + [
#    'django_browserid.context_processors.browserid_form',
#]

# Always generate a CSRF token for anonymous users.
#ANON_ALWAYS = True

# Tells the extract script what files to look for L10n in and what function
# handles the extraction. The Tower library expects this.
#DOMAIN_METHODS['messages'] = [
#    ('%s/**.py' % PROJECT_MODULE,
#        'tower.management.commands.extract.extract_tower_python'),
#    ('%s/**/templates/**.html' % PROJECT_MODULE,
#        'tower.management.commands.extract.extract_tower_template'),
#    ('templates/**.html',
#        'tower.management.commands.extract.extract_tower_template'),
#],

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['lhtml'] = [
#    ('**/templates/**.lhtml',
#        'tower.management.commands.extract.extract_tower_template'),
# ]

# # Use this if you have localizable JS files:
# DOMAIN_METHODS['javascript'] = [
#    # Make sure that this won't pull in strings from external libraries you
#    # may use.
#    ('media/js/**.js', 'javascript'),
# ]

LOGGING = dict(loggers=dict(playdoh = {'level': logging.DEBUG}))

# by default, no special options set up
LDAP_GLOBAL_OPTIONS = {}
