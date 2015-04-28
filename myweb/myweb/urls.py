from django.conf.urls import patterns, include, url
from app01 import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^add$',views.add), #点击按钮来添加新数据的映射
	url(r'^index.html$',views.query), #查询所有数据的映射
	url(r'^add.html$',views.beginAdd), #单独添加新数据的映射
	url(r'^delete$',views.delByID), #点击按钮来删除用户对应数据的映射(根据id)
	url(r'^update$',views.updateByID), #点击按钮来修改用户对应数据的映射(根据id)
	
)
