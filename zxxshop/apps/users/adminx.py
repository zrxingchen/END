

import xadmin
from xadmin import views
from users.models import UserProfile

class BaseSetting(object):
    '''
    xadmin的基础配置
    '''
    enable_themes = True # 开启主题功能
    use_bootswatch = True

class GlobalSettings(object):
    '''
        设置网站标题和页脚
    '''
    site_title = "海马生鲜后台管理页面"
    site_footer = "Powered By 1905C - 2020"
    menu_style = 'accordion'





class UserProfileAdmin(object):
    list_display = ('username','email')
    search_fields = ('name','email')
    list_filter = ('name','email')
    model_icon = 'fa fa-bug'


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile,UserProfileAdmin)