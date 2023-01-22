from django.contrib import admin
from .models import Cortar_url

class Cortar_urlAdmin(admin.ModelAdmin):
    readonly_fields = ('create', )

# Register your models here.
admin.site.register(Cortar_url, Cortar_urlAdmin)
