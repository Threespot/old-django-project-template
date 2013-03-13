DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Django debug toolbar and Django extensions are both highly useful
# utilities. To install them, run::
#
#    ?> pip install {{ project_name }}/requirements-dev.txt
#
INSTALLED_APPS_ENV_ADDITIONS = (
    'debug_toolbar',
    'django_extensions',
)

MIDDLEWARE_CLASSES_ENV_ADDITIONS = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# This function is used to determine when the debug toolbar should be
# displayed: when the user is logged in and not in the admin.
def _ddt_check(request):
    if request.path.startswith("/admin/"):
        return False
    if request.user.is_authenticated():
        return True
    return False

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': _ddt_check
}

# Log sent emails to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Don't compress any static files.
COMPRESS_ENABLED = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': "/tmp/{{ project_name }}_file_cache",
    }
}