"""
WSGI configuration for the BookMySeat Django project.

This module exposes the WSGI application as the module-level
variable `application`.
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "bookmyseat.settings",
)

application = get_wsgi_application()

# Optional alias for platforms/configurations expecting `app`
app = application
