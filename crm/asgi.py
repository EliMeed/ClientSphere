
"""
ASGI entrypoint (WebSocket/async support). Use for ASGI servers (e.g., uvicorn/daphne).
"""


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')

application = get_asgi_application()
