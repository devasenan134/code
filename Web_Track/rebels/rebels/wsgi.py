"""
WSGI config for rebels project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rebels.settings')

application = get_wsgi_application()


import sys

sys.path.append('C:/Users/Deva/Documents/CS/Web_Track/rebels/rebels')
sys.path.append('C:/Users/Deva/Documents/CS/Web_Track/rebels')