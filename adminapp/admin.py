from django.contrib import admin

# Register your models here.
from .models import user,music,musicz

admin.site.register(user)

admin.site.register(music)
admin.site.register(musicz)