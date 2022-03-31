from django.contrib import admin
from .models import Region, Province, Commune, Business
# Register your models here.

admin.site.register(Region)
admin.site.register(Province)
admin.site.register(Commune)
admin.site.register(Business)