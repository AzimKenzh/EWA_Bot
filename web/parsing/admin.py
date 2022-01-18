from django.contrib import admin
from django import forms
from flat_json_widget.widgets import FlatJsonWidget
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from parsing.models import Ebay, Amazon, ImportExcels, EbayAll


@admin.register(Ebay)
class AdminEbay(admin.ModelAdmin):
    list_display = ['id', 'title', 'quantity', 'percent', 'similarity']
    list_display_links = ['id', 'title']


@admin.register(EbayAll)
class AdminEbayAll(admin.ModelAdmin):
    list_display = ['id', 'title', 'quantity', 'percent', 'similarity']
    list_display_links = ['id', 'title']


@admin.register(Amazon)
class AdminAmazon(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']


class JsonDocumentFormSite(forms.ModelForm):
    class Meta:
        widgets = {
            'annotations': FlatJsonWidget,
        }


@admin.register(ImportExcels)
class AdminImportExcel(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ['id', 'title']
    form = JsonDocumentFormSite


