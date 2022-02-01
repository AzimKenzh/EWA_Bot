from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters, status

# from parsing.amazon import amazon_main
from parsing.ebay import ebay_main
from parsing.serializers import *


class ProductTitleViewSet(viewsets.ModelViewSet):
    queryset = ImportExcels.objects.all().order_by('-status')
    serializer_class = ImportExcelSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']

    def create(self, request, *args, **kwargs):
        # delete before creating new items from import
        ImportExcels.objects.all().delete()
        # importing
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'])
    def parse(self, request, pk=None):
        instance = self.get_object()
        instance.status = 'parsing'
        instance.save()

        # start parse here
        ebay_main(instance)
        instance.status = 'parsed'
        instance.save()
        return Response('OK')

    # @action(detail=True, methods=['post'])
    # def parse_amazon(self, request, pk=None):
    #     instance = self.get_object()
    #     instance.status = 'parsing'
    #     instance.save()
    #
    #     # start parse here
    #     # amazon_main(instance)
    #     instance.status = 'parsed'
    #     instance.save()
    #     return Response('OK')


class AllParseAPIView(APIView):
    def post(self, request):
        queryset = ImportExcels.objects.exclude(status__in=['parsing', 'parsed'])
        for instance in queryset:
            instance.status = 'parsing'
            instance.save()

            # start parse here
            # amazon_main(instance)
            ebay_main(instance)
            instance.status = 'parsed'
            instance.save()

        return Response('OK')


# class AllParseAmazonAPIView(APIView):
#     def post(self, request):
#         queryset = ImportExcels.objects.exclude(status__in=['parsing', 'parsed'])
#         for instance in queryset:
#             instance.status = 'parsing'
#             instance.save()
#
#             # start parse here
#             amazon_main(instance)
#             instance.status = 'parsed'
#             instance.save()
#
#         return Response('OK')


class ResultsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ImportExcels.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [IsAuthenticated, ]

    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # search_fields = ['ebayss__title']

    # def get_queryset(self):
    #     queryset = self.filter_queryset(self.queryset)
    #     title_query = self.request.query_params.get('search')
    #     if title_query:
    #         queryset = queryset.filter(ebayss__title__icontains=title_query)
    #     return queryset


class CountStatusAPIView(APIView):
    def get(self, request):
        parsed_count = ImportExcels.objects.filter(status=ImportExcels.STATUS[3][0]).count()
        parsing_count = ImportExcels.objects.filter(status=ImportExcels.STATUS[2][0]).count()
        imported_count = ImportExcels.objects.filter(status__in=[ImportExcels.STATUS[0][0],
                                                                 ImportExcels.STATUS[1][0]]).count()
        return Response({'parsed': parsed_count, 'parsing': parsing_count, 'imported': imported_count})


class SearchApiView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('search', '')
        title = Ebays.objects.all()
        if query:
            title = title.filter(title__icontains=query)
            return Response({
                'ebays': EbaysInlineSerializerAdmin(title, many=True).data,
            })
        return Response([])
