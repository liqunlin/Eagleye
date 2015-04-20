from django.conf.urls import patterns, include, url
from app01 import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^add$',views.add), #添加数据的映射
	url(r'^index.html$',views.query), #展现所有数据的映射
	url(r'^add.html$',views.beginAdd), #访问添加首页的html 的映射
	url(r'^delete$',views.delByID), #根据id来删除用户 的映射
	url(r'^showid$',views.showUid), #根据id来更新 的映射
	
)
