INSTALLED_APPS = [
...,
'rest_framework',
'drf_spectacular',
'corsheaders',
'apps.accounts',
'apps.courses',
]


MIDDLEWARE = [
'corsheaders.middleware.CorsMiddleware',
...
]


REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
'rest_framework_simplejwt.authentication.JWTAuthentication',
),
'DEFAULT_PERMISSION_CLASSES': (
'rest_framework.permissions.IsAuthenticated',
),
'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


SIMPLE_JWT = {
'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}


AUTH_USER_MODEL = 'accounts.User'


# CORS
CORS_ALLOWED_ORIGINS = [
'http://localhost:3000',
]


# drf-spectacular
SPECTACULAR_SETTINGS = {
'TITLE': 'E-Learning API',
'DESCRIPTION': 'API for e-learning platform',
'VERSION': '1.0.0',
}