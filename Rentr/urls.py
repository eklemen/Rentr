from django.conf.urls import patterns, include, url
from django.contrib import admin
from RentrApp import views
from Rentr import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Rentr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', auth_views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'rentable/$', views.RentableList.as_view(), name='rentableList'),
    url(r'rentable/(?P<pk>[0-9]+)/$', views.RentableDetail.as_view(), name='rentable'),
    url(r'store/(?P<pk>[0-9]+)/$', views.StoreDetail.as_view(), name='store'),
)

