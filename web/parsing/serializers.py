from rest_framework import serializers


class EbaySerializer(serializers.Serializer):
    url = serializers.URLField()
