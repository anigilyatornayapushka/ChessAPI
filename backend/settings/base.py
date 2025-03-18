# Python
from pathlib import Path
import sys
import os
import mimetypes
# Third party
import decouple


BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'dirs'))

SECRET_KEY = decouple.config('SECRET_KEY', cast=str)

DEBUG = decouple.config('DEBUG', cast=bool)

ALLOWED_HOSTS = (
    'localhost',
    '127.0.0.1',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'rest_framework_simplejwt',
)

CUSTOM_APPS = (

)

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'settings.urls'

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            'templates',
        ),
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
)

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': decouple.config('DB_NAME', str),
        'USER': decouple.config('DB_USER', str),
        'PASSWORD': decouple.config('DB_PASS', str),
        'HOST': decouple.config('DB_HOST', str),
        'PORT': decouple.config('DB_PORT', str),
    }
}

AUTH_PASSWORD_VALIDATORS = (
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
)

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Russia/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DEBUG TOOLBAR
mimetypes.add_type('application/javascript', '.js', True)

INTERNAL_IPS = (
    '127.0.0.1',
)
