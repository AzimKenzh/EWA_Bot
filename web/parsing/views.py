import timeit

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from parsing.amazon import amazon_main
from parsing.ebay import ebay_main
from parsing.serializers import *
from parsing.walmart import walmart_main


class EbayAPIView(APIView):
    def get(self, request):
        urls = ebay_main()
        return Response(urls)

    def save(self):
        self.serializer = EbaySerializer


class WalmartAPIView(APIView):
    def get(self, request):
        data = walmart_main()
        return Response(data)

    # def save(self):
    #     self.serializer = WalmartSerializer


class AmazonAPIView(APIView):
    def get(self, request):
        dict_ = amazon_main()
        serializer = AmazonSerializer(instance=dict_, many=True)
        return Response(serializer.data)

    def save(self):
        self.serializer = AmazonSerializer


class EbayAdminViewSet(viewsets.ModelViewSet):
    queryset = Ebay.objects.all()
    serializer_class = EbaySerializerAdmin


class AmazonAdminViewSet(viewsets.ModelViewSet):
    queryset = Amazon.objects.all()
    serializer_class = AmazonSerializerAdmin


class WalmartAdminViewSet(viewsets.ModelViewSet):
    queryset = Walmart.objects.all()
    serializer_class = WalmartSerializerAdmin


