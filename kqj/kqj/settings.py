"""
Django settings for kqj project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '95flp1#%0ny8eef*rwx2s8wndk7&bp#9i^8#gnt*iwb3bsj-s7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'data',
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

ROOT_URLCONF = 'kqj.urls'

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

WSGI_APPLICATION = 'kqj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'know',
        'USER': 'know',
        'PASSWORD': 'know',
        'HOST': '120.79.41.9',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


SUIT_CONFIG = {
    'ADMIN_NAME': 'evaluate',
    # 'ADMIN_NAME': 'TSWGAIMS',
    'HEADER_DATE_FORMAT': 'Y-m-d l',
    'HEADER_TIME_FORMAT': 'H:i',
    # forms
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    # menu
    'LIST_PER_PAGE': 10,
    'MENU_OPEN_FIRST_CHILD': True,
    'MENU': (
                'sites',

                {'label': '平台管理团队',
                  'app': 'incubator',
                  'models': (
                            'Incubator','index.Bonus','index.Subtraction','institution.InvestReport',

                            {'label': '企业评估报告', 'url': '/admin/institution/report'},
                            {'label': '资产负债表', 'url': '/admin/company/balance'},

                )},

                  
                {'label': '基本信息',
                  'app': 'company',
                  'models': (
                            {'label': '企业基本信息', 'url': '/admin/company/companyinfo_opt'},
                            'CoreMember','IndependentEvaluationOfEnterprises',
                            # 'FinancialSituation','ProductsAndMarket','TechnologyRD','ServerRequest',
                            {'label': '资产负债表', 'url': '/admin/company/balance'},
                            {'label': '利润表', 'url': '/admin/company/profit'},
                            {'label': '现金流量表', 'url': '/admin/company/cash_flow'},

                )},


                  





             ),
        # 每一个字典表示左侧菜单的一栏
    # label表示name，app表示上边的install的app，modelRs表示用了哪些modelsf 
}