import os
import sys

# Přidej cestu k adresáři projektu do Python path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.insert(0, path)

# Nastav Django settings modul
os.environ['DJANGO_SETTINGS_MODULE'] = 'svodex_web.settings'

# Importuj a získej WSGI aplikaci
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Tento řádek je klíčový pro nasazení na Vercel
app = application