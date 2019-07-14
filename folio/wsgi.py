"""
WSGI config for folio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv.read_dotenv(os.path.join(BASE_DIR, '.env'), override=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'folio.settings')

application = get_wsgi_application()
