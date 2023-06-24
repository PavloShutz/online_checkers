"""
ASGI config for OnlineCheckers project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineCheckers.settings')

application = get_asgi_application()
