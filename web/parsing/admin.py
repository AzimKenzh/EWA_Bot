from django.contrib import admin

from parsing.models import Ebay, Walmart, Amazon, ImportExcel


@admin.register(Ebay)
class AdminEbay(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'created_at']
    list_display_links = ['id', 'title']


@admin.register(Amazon)
class AdminAmazon(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']


@admin.register(Walmart)
class AdminWalmart(admin.ModelAdmin):
    list_display = ['id', 'title', 'url']
    list_display_links = ['id', 'title']


@admin.register(ImportExcel)
class AdminImportExcel(admin.ModelAdmin):
    list_display = ['id', 'title']

