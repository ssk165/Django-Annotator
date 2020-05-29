from django.contrib import admin

# Register your models here.
from .models import Annotation, CharacterSet

admin.site.register(Annotation)
admin.site.register(CharacterSet)
