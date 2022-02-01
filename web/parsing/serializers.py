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


class EbayAllSerializerAdmin(serializers.ModelSerializer):
    title = serializers.CharField(max_length=800, required=False)
    url = serializers.URLField(required=False)

    class Meta:
        model = EbayAll
        fields = '__all__'


class EbaysSerializerAdmin(serializers.ModelSerializer):
    title = serializers.CharField(max_length=800, required=False)
    url = serializers.URLField(required=False)

    class Meta:
        model = Ebays
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


class ImportExcelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImportExcels
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['status'] = instance.get_status_display()
        return representation


class ResultsSerializer(serializers.ModelSerializer):
    ebay = EbaySerializerAdmin(required=False)
    ebay_all = EbayAllSerializerAdmin(required=False)
    ebays = EbaysSerializerAdmin(required=False)
    # amazon = AmazonSerializerAdmin(required=False)

    class Meta:
        model = ImportExcels
        fields = ('id', 'title', 'ebay', 'ebay_all', 'ebays')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ebay'] = EbaySerializerAdmin(instance.ebays.all(), many=True, context=self.context).data
        representation['ebay_all'] = EbayAllSerializerAdmin(instance.ebaysall.all(), many=True, context=self.context).data
        representation['ebays'] = EbaysSerializerAdmin(instance.ebayss.all(), many=True, context=self.context).data
        # representation['amazon'] = AmazonSerializerAdmin(instance.amazons.all(), many=True, context=self.context).data
        return representation


# class AmazonSerializerAdmin(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=800, required=False)
#     url = serializers.URLField(required=False, max_length=900)
#
#     class Meta:
#         model = Amazon
#         fields = '__all__'