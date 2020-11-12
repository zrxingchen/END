
import xadmin
from django.urls import path,include


from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework import routers

schema_view = get_schema_view(title='corejson')
from apps.course.views import CourseListViewSet

router = routers.DefaultRouter()
router.register('goods',CourseListViewSet)
urlpatterns = [
    path('xadmin/', xadmin.site.urls),

    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),
    path('docs/',include_docs_urls(title='DRF文档')),
    path('schema/',schema_view),
]
