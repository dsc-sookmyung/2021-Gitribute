import os, json
from django.core.exceptions import ImproperlyConfigured
from pathlib import Path
from datetime import timedelta, datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'account',
]

AUTH_USER_MODEL = 'account.User'

## DRF 
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', # 인증된 사용자만 접근 가능
        'rest_framework.permissions.IsAdminUser', # 관리자만 접근 가능
        'rest_framework.permissions.AllowAny', # 누구나 접근 가능

    ),

    'DEFAULT_RENDERER_CLASSES': (
        # 자동으로 json으로 바꿔줌
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),


    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
}

## JWT
# 추가적인 JWT_AUTH 설젇
JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256', # 암호화 알고리즘
    'JWT_ALLOW_REFRESH': True, # refresh 사용 여부
    'JWT_EXPIRATION_DELTA': timedelta(days=30), # 유효기간 설정
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=30), # JWT 토큰 갱신 유효기간
    # import datetime 상단에 import 하기
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Gitribute_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Gitribute_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'gitribute',
        'USER':'root',
        'PASSWORD':get_secret("DATABASE"),
        'HOST':'34.123.113.216',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
