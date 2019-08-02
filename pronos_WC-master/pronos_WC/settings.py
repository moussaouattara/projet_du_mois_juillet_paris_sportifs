# -*- coding: utf-8 -*-

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.core.urlresolvers import reverse_lazy
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_PATH = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

path = lambda *a: os.path.join(*a)
project_path = lambda *a: os.path.join(PROJECT_ROOT, *a)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1(desl5*u)(j4i+f!z*ro=i#8rvx(ht)c)scqu8mwu^bm-=as%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    project_path('templates'),
)
print(TEMPLATE_DIRS)
# Application definition

DJANGO_APPS = (
    'suit',  # Interface admin (w/ Bootstrap)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'south',  # Migrations
    'django_extensions',
    'imagekit',
    'profiles',
    'ckeditor',
    'crispy_forms',
)    

PROJECT_APPS = (
    'pronos_WC.apps.football',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pronos_WC.urls'

WSGI_APPLICATION = 'pronos_WC.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'
LANGUAGES = (
    ('fr', 'Français'),
)
DEFAULT_LANGUAGE = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
        'NAME': 'pronos_WC',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = os.path.normpath(os.path.join(BASE_PATH, 'media'))
MEDIA_URL = '/media/'


STATIC_ROOT = project_path('public', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    project_path('static'),
)

CKEDITOR_UPLOAD_PATH = MEDIA_ROOT
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
    },
}

AUTH_PROFILE_MODULE = 'profiles.UserProfile'

LOGIN_URL = 'pronos_WC_login'
LOGOUT_URL = 'pronos_WC_logout'
LOGIN_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
