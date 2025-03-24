from pathlib import Path
import os

# Seguridad
from decouple import config

# Claves secretas y modo debug (ajustar en producción)
SECRET_KEY = config('SECRET_KEY', default='fNwSf2g5RixBazevRNW2-lVhNlBFXCbkNppTVfOVae7PdYX_rQ0vb1i09ThDPRcrAl0')
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.vercel.app']

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Hosts permitidos para acceder al proyecto
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.vercel.app']

# Aplicaciones instaladas en el proyecto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portafolio_app',
]

# Middlewares necesarios
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Archivo de enrutamiento principal
ROOT_URLCONF = 'portafolio.urls'

# Configuración de plantillas HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Habilito una carpeta global para plantillas
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

# Configuración del servidor WSGI
WSGI_APPLICATION = 'portafolio.wsgi.application'

# Configuración de la base de datos (SQLite, ajustable a otras)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validación de contraseñas
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

# Configuración de internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'  # URL base para servir archivos estáticos
STATICFILES_DIRS = [BASE_DIR / 'portafolio_app/static']  # Rutas donde buscar archivos estáticos
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Carpeta de destino para los archivos recopilados (collectstatic)

# Configuración de archivos multimedia (opcional, si necesitas subir archivos)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Tipo de campo para claves primarias automáticas
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SECURE_SSL_REDIRECT = False
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
