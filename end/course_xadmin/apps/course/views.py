from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets


from apps.course.serializers import CourseSerializer
from .models import Course
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class CoursePagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100

class CourseListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
        list:
            商品列表，分页，搜索，过滤，排序
        retrieve:
            获取商品详情
    '''
    pagination_class = CoursePagination
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    #设置搜索
    search_fields = ("name",'goods_brief','goods_desc')
    # 排序
    ordering_fields = ('sold_num','shop_price')