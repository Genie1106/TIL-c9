from django.contrib import admin
from .models import Music, Comment, Artist

# Register your models here.
admin.site.register(Music)
admin.site.register(Artist)
admin.site.register(Comment)