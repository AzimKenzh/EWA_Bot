from rest_framework import serializers

from parsing.models import *


class EbaySerializer(serializers.Serializer):
    url = serializers.URLField()


class EbaySerializerAdmin(serializers.ModelSerializer):
    title = serializers.CharField(max_length=800, required=False)
    url = serializers.URLField(required=False)

    class Meta:
        model = Ebay
        fields = '__all__'


class EbaySerializerExport(serializers.ModelSerializer):
    title = serializers.CharField(max_length=800, required=False)
    url = serializers.URLField(required=False)

    class Meta:
        model = Ebay
        exclude = ('id', )


class AmazonSerializer(serializers.Serializer):
    url = serializers.URLField()
    title = serializers.CharField(max_length=200)


class AmazonSerializerAdmin(serializers.ModelSerializer):
    title = serializers.CharField(max_length=800, required=False)
    url = serializers.URLField(required=False, max_length=900)

    class Meta:
        model = Amazon
        fields = '__all__'


# class WalmartSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     url = serializers.URLField()
#     shipping = serializers.CharField(max_length=200)
#     quantity = serializers.CharField(max_length=200)
#     # quantity = serializers.CharField(max_length=200)
#
#
# class WalmartSerializerAdmin(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=800, required=False)
#     url = serializers.URLField(required=False)
#
#     class Meta:
#         model = Walmart
#         fields = '__all__'


class ImportExcelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImportExcels
        fields = '__all__'


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportExcels
        fields = ('id', 'title')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ebey'] = EbaySerializerAdmin(instance.ebays.all(), many=True, context=self.context).data
        representation['amazon'] = AmazonSerializerAdmin(instance.amazons.all(), many=True, context=self.context).data
        return representation