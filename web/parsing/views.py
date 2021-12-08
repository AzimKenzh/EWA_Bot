import codecs
import csv
import timeit

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters

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

    def save(self):
        self.serializer = WalmartSerializer


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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', ]


class AmazonAdminViewSet(viewsets.ModelViewSet):
    queryset = Amazon.objects.all()
    serializer_class = AmazonSerializerAdmin
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', ]


class WalmartAdminViewSet(viewsets.ModelViewSet):
    queryset = Walmart.objects.all()
    serializer_class = WalmartSerializerAdmin


class ImportExcelViewSet(viewsets.ModelViewSet):
    queryset = ImportExcels.objects.all()
    serializer_class = ImportExcelSerializer








    # ebay = open('ebay.csv', 'wb')
    # c = csv.writer(ebay)
    #
    # query = ("SELECT * from, id2_active from table1")
    #
    # cursor.execute(query)



# @permission_classes([IsMonSpecialist, IsManager, IsAdmin])
# def export_csv(request, survey_id):
#     """
#     Export survey data as excel spreadsheet VERS2
#     """
#     user_responses = UserResponses.objects.filter(survey_id=survey_id)
#     questions = Question.objects.filter(survey_id=survey_id)
#     question_text = questions.values("text")
#
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = f'attachment; filename=survey_results_{survey_id}.csv'
#
#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         with codecs.open(f"{output.name}", "w", encoding="cp1251") as stream:
#             writer = csv.writer(stream, quoting=csv.QUOTE_ALL)
#             writer.writerow(["ID Ученика", *[text["text"] for text in question_text]])
#             for response_ in user_responses:
#                 answers = response_.response_answers.all()
#                 writer.writerow([response_.interviewer.student_code, *[str(answer.body)[1:-1] for answer in answers]])
#         output.seek(0)
#         response.write(output.read())
#     return response