from django.contrib import admin
from app_api_tutorial.models import Tutorial

class Tutorials(admin.ModelAdmin):

    list_display = ('id', 'title')
    list_per_page = 10

admin.site.register(Tutorial, Tutorials)
