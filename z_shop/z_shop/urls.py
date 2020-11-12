
import xadmin
from django.urls import path,include,re_path
from django.views.static import serve
from z_shop.settings import MEDIA_ROOT

from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import GoodsListViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewset,UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset


router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViewSet)

router.register('categorys', CategoryViewSet,basename="categorys")
router.register(r'code', SmsCodeViewset, basename="code")
router.register(r'userfavs', UserFavViewset, basename="userfavs")
router.register(r'messages', LeavingMessageViewset, basename="messages")
router.register(r'address',AddressViewset , basename="address")
router.register(r'shopcarts', ShoppingCartViewset, basename="shopcarts")
router.register(r'orders', OrderViewset, basename="orders")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/',include('DjangoUeditor.DjangoUeditor.u'
                            'rls')),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    # path('goods/',GoodsListView.as_view(),name='goods-list'),
    path('docs',include_docs_urls(title='Dom-sub')),
    path('api-auth/',include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),

    re_path('^', include(router.urls)),
    path('jwt-auth/', obtain_jwt_token),
    path('docs',include_docs_urls(title='Dom-sub')),
]
