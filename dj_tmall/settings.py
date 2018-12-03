"""
Django settings for dj_tmall project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 加密密钥
SECRET_KEY = 'dlk%=h5#-fg*mkxq$!vs+i&-6d@85pg(jbigqt#6ds9kt^@)3d'

# 开发模式（上线设置为False）
DEBUG = True
# 允许访问的ip地址（上线需要配置）
ALLOWED_HOSTS = []


# 注册系统app
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 注册第三方app
EXT_APPS = [
    'xadmin',
    'crispy_forms',
    # 修改主题
    'reversion',
    #跨域插件
    'corsheaders',
]

# 注册自定义app
CUSTOM_APPS = [
    'apps.account',
    'apps.cate',
    'apps.detail',
    'apps.main',
    'apps.search',
]

# 拼接apps
INSTALLED_APPS = SYS_APPS + EXT_APPS + CUSTOM_APPS

# 注册中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #跨域
    # 'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.common.CommonMiddleware',
]

#允许所有跨域请求
# CORS_ORIGIN_ALLOW_ALL=True

# 根路由配置，一般不需要修改
ROOT_URLCONF = 'dj_tmall.urls'
# NUMBER=

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                os.path.join(BASE_DIR, 'apps/main/templates'),
                os.path.join(BASE_DIR, 'apps/cart/templates')
                 ]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            # 模板全局配置变量
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.cart.context_processors.count',
            ],
        },
    },
]

# 启动应用程序配置（一般不需要修改）
WSGI_APPLICATION = 'dj_tmall.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# 数据库配置
DATABASES = {
    # 默认数据库配置（可以配置多个）
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj_tmall',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

# 用户密码验证配置（一般不需要修改）
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

LOGIN_URL='/account/login/'
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# 语言配置（开发中设置为中文
LANGUAGE_CODE = 'zh-hans'
# 时区设置，设置为中国时区
TIME_ZONE = 'Asia/Shanghai'
# 国际化配置，自动转化多国语言
USE_I18N = True
# 国际化配置，自动转化多国语言
USE_L10N = True
# 开启django时区，如果不需要django时区可以设置为False（建议设置为False）
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# 访问静态文件的路径配置
STATIC_URL = '/static/'

# 静态文件目录配置
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'apps/main/static'),
)

# 配置访问多媒体的路径
MEDIA_URL = '/media/'

# 配置文件上传目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 缓存配置
# 使用pip install django-redis安装
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         # 缓存地址
#         'LOCATION': 'redis://127.0.0.1:6379',
#         'OPTIONS': {
#             # 如果有密码，添加密码配置
#             # 'PASSWORD':123
#             # 使用线程池管理连接
#             'CONNECTION_POOL_KWARGS': {'max_connections': 100}
#         }
#     },
#     'session': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         # 缓存地址
#         'LOCATION': 'redis://127.0.0.1/2',
#         'OPTIONS': {
#             'CONNECTIONS_POOL_KWARGS': {'max_connections': 100}
#         }
#     },
# }

# session缓存配置
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_CACHE_ALIAS = 'session'
#
# # session失效时间 7天(默认两周）
# SESSION_COOKIE_AGE = 7 * 24 * 60 % 60

# =======邮件配置=======
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'jingyetong@163.com'
EMAIL_HOST_PASSWORD = 'jinye123'
EMAIL_USE_TLS = True

# =======日志配置=======
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
