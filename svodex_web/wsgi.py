import os
import sys

from django.core.wsgi import get_wsgi_application

# Cesta k projektu
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Nastavení pro Vercel
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'svodex_web.settings')

# WSGI aplikace
application = get_wsgi_application()

# Klíčový řádek pro Vercel
app = application