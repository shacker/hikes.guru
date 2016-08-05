import os
import sys
from django.contrib.messages import constants as message_constants

DEBUG = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'project/static'), ]

# os.path.dirname refs the parent dir
LOGGING_DIR = os.path.join(BASE_DIR, 'project/logs')
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/uploads/'
STATIC_ROOT = os.path.join(BASE_DIR, 'project/static_deploy')  # collectstatic will gather static files here.
STATIC_URL = '/static/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
]

INTERNAL_IPS = ['127.0.0.1', ]
ALLOWED_HOSTS = [
    '.hikes.guru',  # Allow domain and subdomains
    '127.0.0.1',
]

# Add our custom 'apps' dir to the path
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

INSTALLED_APPS = [
    # Django built-ins
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    # 3rd party
    'django_extensions',
    'social.apps.django_app.default',
    'bootstrapform',
    # 'autofixture',

    # Our apps
    'base',
    'people',
    'trails',
    'feedback',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['project/templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

# HTML tags users are allowed to use in forms - all others are bleached out
ALLOWED_TAGS = [
    'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i',
    'li', 'ol', 'strong', 'ul', 'p', 'h1', 'h2', 'h3', 'h4', 'hr'
    ]

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/login/twitter'

WSGI_APPLICATION = 'project.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True

AUTH_USER_MODEL = 'people.UserProfile'

# Because we are proxying through nginx, trust the forwarded hostname
USE_X_FORWARDED_HOST = True

# Override CSS class for the ERROR tag level to match Bootstrap class name
MESSAGE_TAGS = {message_constants.ERROR: 'danger'}

# HTML tags users are allowed to use in forms - all others are bleached out
ALLOWED_TAGS = [
    'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li',
    'ol', 'strong', 'ul', 'p', 'h1', 'h2', 'h3', 'h4', 'hr', 'br',
    ]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
        'TIMEOUT': 86400,  # 5 minutes
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s:%(lineno)s %(message)s',
            'datefmt': "%m/%d/%Y %H:%M:%S",
        },
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(name)s:%(lineno)s %(process)d %(thread)d %(message)s',
            'datefmt': "%m/%d/%Y %H:%M:%S",
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'standard',
        },
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'all.log'),
            'maxBytes': 1024*1024*512,  # 0.5G
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'request_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'django_request.log'),
            'maxBytes': 1024*1024*512,  # 0.5G
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['request_file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['log_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
