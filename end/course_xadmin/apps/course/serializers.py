from rest_framework import  serializers
from  rest_framework import serializers
from django.db.models import Q
from .models import Course
from rest_framework import routers



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'