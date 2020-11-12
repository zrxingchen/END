from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework.response import Response


# 原先views 视图
#
# class GoodsListView(APIView):
#     '''
#     商品列表
#     '''
#     def get(self,request,format=None):
#         goods = Goods.objects.all()
#         goods_serialzer = GoodsSerializer(goods,many=True)
#         return Response(goods_serialzer.data)

from rest_framework.views import APIView
from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .filters import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status

class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100


# class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
#     '商品列表页'
#
#     #这里必须要定义一个默认的排序,否则会报错
#     queryset = Goods.objects.all()
#     # 分页
#     pagination_class = GoodsPagination
#     #序列化
#     serializer_class = GoodsSerializer
#     filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
#
#     # 设置filter的类为我们自定义的类
#     #过滤
#     filter_class = GoodsFilter
#     #搜索,=name表示精确搜索，也可以使用各种正则表达式
#     search_fields = ('=name','goods_brief')
#     #排序
#     ordering_fields = ('sold_num', 'add_time')


class GoodsListView(APIView):
    """
    List all goods
    """

    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request, format=None):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)