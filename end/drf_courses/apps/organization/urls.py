from django.urls import path,include
from organization import views

urlpatterns = [

    path('oav/list',views.CourseOrgViewSet.as_view(),name='oav-list'),
    path('obv/list',views.TeacherViewSet.as_view(),name='obv-list'),
    path('ocv/list',views.CityDictViewSet.as_view(),name='ocv-list'),


]