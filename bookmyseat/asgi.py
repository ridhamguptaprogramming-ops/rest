"""
ASGI configuration for the BookMySeat Django project.

This module exposes the ASGI application as a module-level
variable named `application`.
"""

import os

from django.core.asgi import get_asgi_application


# Tell Django which settings module to use.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "bookmyseat.settings",
)


# Create the ASGI application.
application = get_asgi_application()
