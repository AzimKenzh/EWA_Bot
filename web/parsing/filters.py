from django_filters import FilterSet
from django_filters import rest_framework as filters

from parsing.models import Ebay, Amazon


class EbayFilter(FilterSet):
    title = filters.CharFilter('title')

    class Meta:
        model = Ebay
        fields = ('title', )


class AmazonFilter(FilterSet):
    title = filters.CharFilter('title')

    class Meta:
        model = Amazon
        fields = ('title', )