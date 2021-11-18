from django.contrib import admin

from parsing.models import Ebay


@admin.register(Ebay)
class AdminEbay(admin.ModelAdmin):
    list_display = ['id', 'title', 'url']
    list_display_links = ['id', 'url']