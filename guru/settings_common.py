import os

DEBUG = False

ADMINS = [
    ('Scot Hacker', 'shacker@birdhouse.org'),
]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'guru/static'), ]

# os.path.dirname refs the parent dir
LOGGING_DIR = os.path.join(BASE_DIR, 'guru/logs')
MEDIA_ROOT = os.path.join(BASE_DIR, 'guru/uploads')
STATIC_ROOT = os.path.join(BASE_DIR, 'guru/static_deploy')  # collectstatic will gather static files here.
STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
]

INTERNAL_IPS = ['127.0.0.1', ]
ALLOWED_HOSTS = [
    '.hikes.guru',  # Allow domain and subdomains
    '127.0.0.1',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'people',
    'hikes',
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

ROOT_URLCONF = 'guru.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['guru/templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'guru.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

AUTH_USER_MODEL = 'people.UserProfile'

# Because we are proxying through nginx, trust the forwarded hostname
USE_X_FORWARDED_HOST = True

WSGI_APPLICATION = 'guru.wsgi.application'

# Override CSS class for the ERROR tag level to match Bootstrap class name
from django.contrib.messages import constants as message_constants
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
