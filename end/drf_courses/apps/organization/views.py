from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CourseOrg,Teacher,CityDict
from .serializers import CityDictSerializer,CourseOrgSerializer,TeacherSerializer

# DRF  CBV   APIView
from rest_framework.views import APIView

class CourseOrgViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = CourseOrg.objects.all().order_by('-date_joined')
    serializer_class = CourseOrgSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = Teacher.objects.all().order_by('-date_joined')
    serializer_class = TeacherSerializer

class CityDictViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = CityDict.objects.all().order_by('-date_joined')
    serializer_class = CityDictSerializer