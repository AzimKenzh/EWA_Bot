import timeit

from rest_framework.response import Response
from rest_framework.views import APIView

from parsing.ebay import main
from parsing.serializers import EbaySerializer


class EbayAPIView(APIView):
    def get(self, request):
        # EBAY_URL = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Softsoap+Liquid+Hand+Soap%2C+Fresh+Breeze++7.5+Oz&_sacat=0&LH_TitleDesc=0&_fsrp=1&rt=nc&LH_PrefLoc=1&LH_ItemCondition=3&LH_All=1&_odkw=maybelline+instant+age+rewind+eraser+dark+circles+treatment+multi-use+concealer+light++0.2+oz&_osacat=0&_dcat=11865&_sop=10&_oaa=1&_fcid=1'
        # EBAY_URL = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=softsoap+liquid+hand+soap%2C+fresh+breeze++7.5+oz&_sacat=0&LH_TitleDesc=0&_fsrp=1&rt=nc&_odkw=maybelline+instant+age+rewind+eraser+dark+circles+treatment+multi-use+concealer+light++0.2+oz&_osacat=0&_dcat=11865&_sop=10&LH_PrefLoc=1&_oaa=1&_fcid=1&LH_All=1'
        # dict_ = []
        dict_ = main()
        # t = timeit.timeit(main, number=1)
        # print(t, 'Totallllllllllllllllllllll')
        serializer = EbaySerializer(instance=dict_, many=True)
        return Response(serializer.data)

    def save(self):
        self.serializer = EbaySerializer
