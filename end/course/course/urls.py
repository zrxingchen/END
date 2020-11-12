
import xadmin
from django.urls import path

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
]
