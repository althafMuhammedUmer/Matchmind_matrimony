
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_b!1(us!bb65w5mz_lfs#^#*d0lx87628a36j8y+bjlc+=wh9&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'main',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Mindmatch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'Mindmatch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'Mindmatch',
#        'USER': 'postgres',
#        'PASSWORD': 'qwedfgbnm',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
# }




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



STATIC_URL = '/static/'

MEDIA_URL = '/media/'



STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'main/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

AUTH_USER_MODEL = 'accounts.CustomUser'


# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTIONS": {
          
#         },
#     },
# }


# AWS_QUERYSTRING_AUTH = False
# DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"
# # STATICFILES_STORAGE = "storages.backends.s3.S3Storage"
# AWS_ACCESS_KEY_ID = 'AKIAZNF5UGMZQH2UUZMW'
# AWS_SECRET_ACCESS_KEY = 'ekFsK0JKQsrh7eZqgOmLzNpxExHAfVtvlbNiJ'
# AWS_STORAGE_BUCKET_NAME= 'Dparol'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AWS_ACCESS_KEY_ID = 'AKIAZNF5UGMZQH2UUZMW'
# AWS_SECRET_ACCESS_KEY = 'ekFsK0JKQsrh7eZqgOmLzNpxExHAfVtvlbNiJ'
# AWS_STORAGE_BUCKET_NAME = 'mindmatch'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = 'public-read'
# AWS_LOCATION = 'static'


# STATICFILES_DIRS = [    
#     BASE_DIR/'static',
    
    
# ]
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# ...
#aws static file configuration
# AWS_STORAGE_BUCKET_NAME = 'mindmatch'
# AWS_ACCESS_KEY_ID = 'AKIAZNF5UGMZQH2UUZMW'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
# AWS_DEFAULT_ACL = 'public-read'

# STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
# MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_LOCATION = 'media'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# if DEBUG:
#     STATICFILES_DIRS = [BASE_DIR / "static"]
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'Static_Files')

# MEDIA_ROOT = ''

# ...
