import os

from django.core.asgi import get_asgi_application
from configurations import importer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventol.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

importer.install()

application = get_asgi_application()
