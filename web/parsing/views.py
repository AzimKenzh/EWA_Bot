from django_filters.rest_framework import DjangoFilterBackend
from firebase_admin import credentials, firestore
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters, status

from parsing.amazon import amazon_main
from parsing.ebay import ebay_main
from parsing.serializers import *
import firebase_admin


certificate_location = './firebase/ewa-bot-d54ca-firebase-adminsdk-zj7gl-5ce88f753c.json'
cred = credentials.Certificate(certificate_location)
firebase_admin.initialize_app(cred)
DB = firestore.client()
FIREBASE_COLLECTION = DB.collection('items')


class ProductTitleViewSet(viewsets.ModelViewSet):
    queryset = ImportExcels.objects.all().order_by('-status')
    serializer_class = ImportExcelSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']

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
            # amazon_main(instance)
            instance.status = 'parsed'
            instance.save()
            document = FIREBASE_COLLECTION.document(str(instance.id))
            document.set({'status': instance.get_status_display()})

        return Response('OK')


class ResultsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ImportExcels.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [IsAuthenticated, ]


class CountStatusAPIView(APIView):
    def get(self, request):
        parsed_count = ImportExcels.objects.filter(status=ImportExcels.STATUS[3][0]).count()
        parsing_count = ImportExcels.objects.filter(status=ImportExcels.STATUS[2][0]).count()
        imported_count = ImportExcels.objects.filter(status__in=[ImportExcels.STATUS[0][0],
                                                                 ImportExcels.STATUS[1][0]]).count()
        return Response({'parsed': parsed_count, 'parsing': parsing_count, 'imported': imported_count})
