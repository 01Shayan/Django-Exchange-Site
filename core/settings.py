import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# PWA Setup
# PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')

SECRET_KEY = 'django-insecure-&h&xac^*pxeujm)sdewfc3b3gk!8t5c+szynq&lsu^9ifgtl(ch)n(k'

DEBUG = True
# DEBUG = False
# TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'unfold',  # unfold
    'unfold.contrib.import_export',  # unfold

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pwa',
    # 'djangopwa',
    'tailwind',
    'theme',
    'django_browser_reload',
    'rest_framework',
    'corsheaders',
    'import_export',

    'currency',  # Index
    'calculator',
    'about',
    'doviz',  # Sakarya Doviz Rates http://www.sakaryadoviz.com.tr/
    'mysql_app',  # mysql Status 
]

# Tailwind Setup
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]

# UNFOLD Setup
UNFOLD = {
    "SITE_HEADER": "FarnazEx Admin Panel"
}

CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE':   'django.db.backends.mysql', 
#         'NAME':     "crazy_einstein", 
#         'USER':     "root",
#         'PASSWORD': "POZLc8ALi4HYRxfhqHBF95CT",
#         'HOST':     "farnazex-mysql",
#         'PORT':     "3306",
#     },
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / '/static/' ---> (collect static)

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    os.path.join(BASE_DIR, 'static'),
]

# MEDIA_URL = 'media/'
# MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# PWA Setup
PWA_APP_NAME = 'FarnazEx'
PWA_APP_DESCRIPTION = "FarnazEx PWA"
PWA_APP_THEME_COLOR = '#d4d4d8'
PWA_APP_BACKGROUND_COLOR = '#d4d4d8'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
	{
		'src': 'static/images/icon-160x160.png',
		'sizes': '160x160'
	}
]
PWA_APP_ICONS_APPLE = [
	{
		'src': 'static/images/icon-160x160.png',
		'sizes': '160x160'
	}
]
PWA_APP_SPLASH_SCREEN = [
	{
		'src': 'static/images/icon.png',
		'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
	}
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
# PWA_APP_DEBUG_MODE = False
# PWA_APP_SHORTCUTS = [
#     {
#         'name': 'Shortcut',
#         'url': '/target',
#         'description': 'Shortcut to a page in my application'
#     }
# ]
# PWA_APP_SCREENSHOTS = [
#     {
#       'src': '/static/img/shayan.icns',
#       'sizes': '750x1334',
#       "type": "image/png"
#     }
# ]
