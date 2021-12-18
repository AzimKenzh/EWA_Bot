from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from parsing.models import Ebay, Amazon, ImportExcels


@admin.register(Ebay)
class AdminEbay(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(Amazon)
class AdminAmazon(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']


@admin.register(ImportExcels)
class AdminImportExcel(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ['id', 'title']

