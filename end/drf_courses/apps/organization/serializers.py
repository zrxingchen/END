from django.contrib.auth.models import User
from .models import CourseOrg,Teacher,CityDict
from rest_framework import serializers




class CourseOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseOrg
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class CityDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityDict
        fields = '__all__'