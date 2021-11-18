from rest_framework.response import Response
from rest_framework.views import APIView

from parsing.ebay import main
from parsing.serializers import EbaySerializer


class EbayAPIView(APIView):
    def get(self, request):
        EBAY_URL = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=maybelline+instant+age+rewind+eraser+dark+circles+treatment+multi-use+concealer+light++0.2+oz&_sacat=0&LH_TitleDesc=0&_fcid=1&_sop=10&LH_ItemCondition=3&_fsrp=1&LH_PrefLoc=1&LH_All=1&rt=nc&_oaa=1&_dcat=11865'
        dict_ = main(EBAY_URL) or []
        serializer = EbaySerializer(instance=dict_, many=True)
        return Response(serializer.data)

    def save(self):
        self.serializer = EbaySerializer
