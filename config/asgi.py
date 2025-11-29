"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django_app = get_asgi_application()


import re
from .fastapi_init import fastapi_app

class PathRouter:
    def __init__(self, django_app, fastapi_app):
        self.django_app = django_app
        self.fastapi_app = fastapi_app

    async def __call__(self, scope, receive, send):
        path = scope.get("path", "")

        if re.match(r"^/fastapi", path):
            return await self.fastapi_app(scope, receive, send)
        return await self.django_app(scope, receive, send)


application = PathRouter(django_app, fastapi_app)

# run command: uvicorn
#poetry run  uvicorn config.asgi:application --reload
