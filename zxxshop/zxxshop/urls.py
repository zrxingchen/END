from django.urls import path,include,re_path
import xadmin
from django.views.static import serve
from zxxshop.settings import MEDIA_ROOT
from apps.goods.view_base import GoodsListView
from rest_framework.documentation import include_docs_urls
# from users.views import SmsCodeViewset



from rest_framework.authtoken import views
from goods.views import GoodsListView
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
router = DefaultRouter()

router.register('goods', GoodsListView,basename='goods'),
# router.register(r'categorys', CategoryViewSet, base_name="categorys"),
# router.register(r'code', SmsCodeViewset, base_name="code"),
# router.register(r'users', UserViewset, base_name="users"),
# router.register(r'userfavs', UserFavViewset, base_name="userfavs"),
# router.register(r'messages', LeavingMessageViewset, base_name="messages"),
# router.register(r'address',AddressViewset , base_name="address")

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls' )),

    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('goods/', GoodsListView.as_view(), name='goods-list'),
    path('docs',include_docs_urls(title='北网生鲜')),
    path('api-auth/',include('rest_framework.urls')),
    re_path('^', include(router.urls)),

    path('jwt-auth/', obtain_jwt_token),
    path('api-token-auth/', views.obtain_auth_token),
]