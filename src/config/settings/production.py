from decouple import config, Csv

# SECRET_KEY
SECRET_KEY = config("SECRET_KEY")

# DEBUG
DEBUG = config("DEBUG", default=False, cast=bool)

# ALLOWED_HOSTS
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT", cast=int),
    }
}
