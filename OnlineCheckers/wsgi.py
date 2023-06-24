"""
WSGI config for OnlineCheckers project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineCheckers.settings')

application = get_wsgi_application()
