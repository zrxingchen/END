from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course,CourseResource,Lesson
from .serializers import CourseSerializer,LessonSerializer,CourseResourceSerializer

# DRF  CBV   APIView
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = Course.objects.all().order_by('-date_joined')
    serializer_class = CourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = Lesson.objects.all().order_by('-date_joined')
    serializer_class = LessonSerializer

class CourseResourceViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = CourseResource.objects.all().order_by('-date_joined')
    serializer_class = CourseResourceSerializer




class CourseList(APIView):
    def get(self,request):
        """

        :param request:
        :return:
        """
        course_list = Course.objects.all()
        course_data = CourseSerializer(instance=course_list,many=True)
        return Response(course_data.data,status=status.HTTP_200_OK)

    def post(self,request):
        """

        :param request:
        :return:
        """
        course_data = CourseSerializer(data=request.data)
        if course_data.is_valid():
            course_data.save(teacher=self.request.user)
            return Response(data=course_data.data,status=status.HTTP_201_CREATED)
        return Response(course_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    @staticmethod
    def get_course(pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return

    def get(self,request,pk):
        course = self.get_course(pk=pk)
        if not course:
            return Response(data={"msg":"没有此课程信息"},status=status.HTTP_404_NOT_FOUND)
        course_data = CourseSerializer(instance=course)
        return Response(course_data.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        course = self.get_course(pk=pk)
        if not course:
            return Response(data={"msg":"没有此课程信息"},status=status.HTTP_404_NOT_FOUND)
        course_data = CourseSerializer(instance=course,data=request.data)
        if course_data.is_valid():
            course_data.save()
            return Response(data=course_data.data,status=status.HTTP_201_CREATED)
        return Response(course_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        course = self.get_course(pk=pk)
        if not course:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseInfoView(APIView):
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        all_resourses = CourseResource.objects.filter(course=course)
        context = {
            "course":course,
            "all_resourses":all_resourses
        }

        return Response(context.data, status=status.HTTP_200_OK)

class LessonList(APIView):
    def get(self,request):
        """

        :param request:
        :return:
        """
        lesson_list = Lesson.objects.all()
        lesson_data = CourseSerializer(instance=lesson_list,many=True)
        return Response(lesson_data.data,status=status.HTTP_200_OK)

    def post(self,request):
        """

        :param request:
        :return:
        """
        lesson_data = LessonSerializer(data=request.data)
        if lesson_data.is_valid():
            lesson_data.save(teacher=self.request.user)
            return Response(data=lesson_data.data,status=status.HTTP_201_CREATED)
        return Response(lesson_data.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseResourceList(APIView):
    def get(self,request):
        """

        :param request:
        :return:
        """
        rescource_list = CourseResource.objects.all()
        resource_data = CourseSerializer(instance=rescource_list,many=True)
        return Response(resource_data.data,status=status.HTTP_200_OK)

    def post(self,request):
        """

        :param request:
        :return:
        """
        resource_data = CourseResourceSerializer(data=request.data)
        if resource_data.is_valid():
            resource_data.save(teacher=self.request.user)
            return Response(data=resource_data.data,status=status.HTTP_201_CREATED)
        return Response(resource_data.errors, status=status.HTTP_400_BAD_REQUEST)