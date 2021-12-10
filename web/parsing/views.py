from pprint import pprint

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters, status

from parsing.amazon import amazon_main
from parsing.ebay import ebay_main
from parsing.serializers import *
# from parsing.walmart import walmart_main


# class EbayAPIView(APIView):
#     def get(self, request):
#         urls = ebay_main()
#         return Response(urls)
#
#     def save(self):
#         self.serializer = EbaySerializer




# class WalmartAPIView(APIView):
#     def get(self, request):
#         data = walmart_main()
#         return Response(data)
#
#     def save(self):
#         self.serializer = WalmartSerializer


# class AmazonAPIView(APIView):
#     def get(self, request):
#         dict_ = amazon_main()
#         serializer = AmazonSerializer(instance=dict_, many=True)
#         return Response(serializer.data)
#
#     def save(self):
#         self.serializer = AmazonSerializer


class EbayAdminViewSet(viewsets.ModelViewSet):
    queryset = Ebay.objects.all()
    serializer_class = EbaySerializerAdmin
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['product_title__id']
    permission_classes = [IsAuthenticated, ]


class AmazonAdminViewSet(viewsets.ModelViewSet):
    queryset = Amazon.objects.all()
    serializer_class = AmazonSerializerAdmin
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['product_title__id']
    permission_classes = [IsAuthenticated, ]


# class WalmartAdminViewSet(viewsets.ModelViewSet):
#     queryset = Walmart.objects.all()
#     serializer_class = WalmartSerializerAdmin


class ProductTitleViewSet(viewsets.ModelViewSet):
    queryset = ImportExcels.objects.all()
    serializer_class = ImportExcelSerializer
    permission_classes = [IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'])
    def parse(self, request, pk=None):
        instance = self.get_object()
        if instance.active == True:
            instance.status = 'parsing'
            instance.save()

            # start parse here
            ebay_main(instance)
            amazon_main(instance)
            instance.status = 'parsed'
            instance.save()
        return Response('OK')


class AllParseAPIView(APIView):
    def post(self, request):
        queryset = ImportExcels.objects.exclude(status__in=['parsing', 'parsed'], active=False)
        for instance in queryset:
            instance.status = 'parsing'
            instance.save()

            # start parse here
            ebay_main(instance)
            amazon_main(instance)
            instance.status = 'parsed'
            instance.save()
        return Response('OK')


class ResultsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ImportExcels.objects.all()
    serializer_class = ResultsSerializer
