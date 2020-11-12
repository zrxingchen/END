from django.urls import path,include
from course import views

urlpatterns = [

    path('cbv/list/',views.CourseList.as_view(),name="cbv-list"),
    path('cbv/detail/<int:pk>/',views.CourseDetail.as_view(),name="cbv-detail"),

    path('cav/list',views.CourseInfoView.as_view(),name='cav-list'),
    path('clv/list',views.LessonList.as_view(),name='clv-list'),
    path('crv/list',views.CourseResourceList.as_view(),name='crv-list'),


]