from django.contrib import admin

from parsing.models import Ebay, Walmart, Amazon


@admin.register(Ebay)
class AdminEbay(admin.ModelAdmin):
    list_display = ['id', 'title', 'url']
    list_display_links = ['id', 'title']


@admin.register(Walmart)
class AdminWalmart(admin.ModelAdmin):
    list_display = ['id', 'title', 'url']
    list_display_links = ['id', 'title']


@admin.register(Amazon)
class AdminAmazon(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
