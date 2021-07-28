# -*- coding: utf-8 -*-

"""WSGI configuration."""

import os
import sys

from django.core.wsgi import get_wsgi_application


# python
sys.path.append('/d2/python_venv/3.8/djchekhov/lib/python3.8/')
sys.path.append('/d2/python_venv/3.8/djchekhov/lib/python3.8/site-packages/')
# django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djchekhov.settings.production')
os.environ.setdefault('PYTHON_EGG_CACHE', '/var/cache/python/.python-eggs')
os.environ.setdefault('TZ', 'America/Chicago')
# wsgi
application = get_wsgi_application()
