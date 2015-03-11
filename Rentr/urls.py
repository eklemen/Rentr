from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Rentr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'rentableObject/$', views.RentableObjectList.as_view(), name='rentableObjectList'),
    url(r'rentableObject/(?P<pk>[0-9]+)/$', views.RentableObjectDetail.as_view(), name='rentableObject'),
)
