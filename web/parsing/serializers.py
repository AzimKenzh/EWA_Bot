from rest_framework import serializers


class EbaySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=300)
    url = serializers.URLField()
    from_ = serializers.CharField(max_length=200)
    # condition = serializers.CharField(max_length=400)
    # seller_information = serializers.CharField(max_length=500)
    #
    # def to_representation(self, instance):
    #     represntaion = super().to_representation(instance)
    #     represntaion[]