"""
Django admin configuration for models (list_display, search_fields, filters).
"""

from django.contrib import admin
from .models import Record



admin.site.register(Record)
