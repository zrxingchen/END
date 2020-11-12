# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets


from apps.goods.serializers import GoodsSerializer, CategorySerializer, BannerSerializer, IndexCategorySerializer
from .models import Goods, GoodsCategory, Banner
from .filters import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# 自定义分页
from rest_framework.pagination import PageNumberPagination

class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100
# class GoodsListView(APIView):
#     def get(self,request,format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods,many=True)
#         return Response(goods_serializer.data)

# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

# class GoodsListView(generics.ListAPIView):
#     pagination_class = GoodsPagination
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

class GoodsListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
        list:
            商品列表，分页，搜索，过滤，排序
        retrieve:
            获取商品详情
    '''
    pagination_class = GoodsPagination
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    # 设置筛选
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = GoodsFilter

    #设置搜索
    search_fields = ("name",'goods_brief','goods_desc')
    # 排序
    ordering_fields = ('sold_num','shop_price')

    # 商品点击数 + 1
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页轮播图
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer

class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    # 获取is_tab=True（导航栏）里面的分类下的商品数据
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["生鲜食品", "酒水饮料"])
    serializer_class = IndexCategorySerializer
