from pathlib import Path
from datetime import timedelta
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-g)k1dievuchq=h!8k+0we43j9%(*t5gmpse9%ur1c(2p^m08#7'
DEBUG = True

# ✅ Allow localhost + Lovable + Cloudflare tunnel
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".trycloudflare.com",  # Wildcard for any tunnel
    "pencil-jewellery-rendering-folding.trycloudflare.com",
    "accessing-bay-bull-oriental.trycloudflare.com",
    "mathematical-job-scholar-toll.trycloudflare.com",
    "tide-distribute-vehicles-temporal.trycloudflare.com",  # ✅ Add your current tunnel here
]

# ----------------------------------------
# Installed Apps
# ----------------------------------------
INSTALLED_APPS = [
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "tracker",
]

# ----------------------------------------
# Middleware
# ----------------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # ✅ Must be on top
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "fitness_backend.urls"

# ----------------------------------------
# Templates
# ----------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "fitness_backend.wsgi.application"

# ----------------------------------------
# Database
# ----------------------------------------
DATABASES = {
    'default': dj_database_url.config(
        default="postgresql://neondb_owner:npg_DlPuiq4MW3rO@ep-sparkling-glitter-a7onck0y-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require",
        conn_max_age=600,
        ssl_require=True,
    )
}

# ----------------------------------------
# Password Validation
# ----------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ----------------------------------------
# Internationalization
# ----------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----------------------------------------
# Django REST Framework & JWT Config
# ----------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# ----------------------------------------
# ✅ CORS Settings (Lovable + Cloudflare + local dev)
# ----------------------------------------
CORS_ALLOWED_ORIGINS = [
    "https://mardi-jim-dynamic-hours.trycloudflare.com",  # ✅ No space at start
    "https://app.lovable.dev",
    "http://localhost:3000",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["authorization", "content-type"]
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]

# ⚠️ Optional (for debugging only; disable in production)
# CORS_ALLOW_ALL_ORIGINS = True
