"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv()

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    os.getenv("DJANGO_SETTINGS_MODULE", "config.settings.dev"),
)

application = get_wsgi_application()
