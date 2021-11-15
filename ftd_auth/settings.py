# Python Imports
import environ
import os
# Django
from django.conf import settings
from django.test.signals import setting_changed
# Rest Framework
from rest_framework.settings import APISettings

# Env Logic
env = environ.Env()

# Take environment variables from .env file
environ.Env.read_env(os.path.join(settings.BASE_DIR, '.env'))

USER_SETTINGS = getattr(settings, 'FTD_AUTH', None)

DEFAULTS = {
    # JWT CUST SETTINGS
    'C_JWT_KEY': 'Leoisnotthebest',
    'C_JWT_TOKEN_EXP': 1000,
    'C_CLIENT_URL': 'http://localhost:3000/', #Default React Host
    'C_SERVER_URL': 'http://localhost:8000/' #Default Django Host
}

api_settings = APISettings(USER_SETTINGS, DEFAULTS)

def reload_api_settings(*args, **kwargs):
    global api_settings

    setting, value = kwargs['settings'], kwargs['value']

    if setting == 'FTD_AUTH':
        api_settings = APISettings(value, DEFAULTS)

setting_changed.connect(reload_api_settings)