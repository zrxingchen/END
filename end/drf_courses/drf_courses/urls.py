
import xadmin
from django.urls import path,include

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from course import views
from organization.views import CourseOrgViewSet,TeacherViewSet,CityDictViewSet
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'lesson', views.LessonViewSet)
router.register(r'courseresource', views.CourseResourceViewSet)
router.register(r'courseorg',CourseOrgViewSet,basename='courseorg')
router.register(r'teacher', TeacherViewSet,basename='teacher')
router.register(r'citydict', CityDictViewSet,basename='citydict')


urlpatterns = [
    path('xadmin/', xadmin.site.urls),

    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('course/',include('course.urls')),
    path('openapi', get_schema_view(
        title="北网titile",
        description="API for all things …"
    ), name='openapi-schema'),
]
