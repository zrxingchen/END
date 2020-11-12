from django.views.generic import View
from goods.models import Goods

class GoodsListView(View):
    def get(self,request):

        json_list = []

        goods = Goods.objects.all()

        import json
        from django.core import serializers
        from django.http import JsonResponse

        json_data = serializers.serialize('json',goods)
        json_data = json.loads(json_data)

        return JsonResponse(json_data,safe=False)