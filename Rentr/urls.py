from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from RentrApp import views
from Rentr import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Rentr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', auth_views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.user_login, name="login"),
    url(r'rentable/$', views.RentableList.as_view(), name='rentable'),
    url(r'rentable/(?P<store>[0-9]+)/$', views.RentableList.as_view(), name='rentableStoreList'),
    url(r'rentable/(?P<pk>[0-9]+)/edit/$', views.make_rental, name='rentableEdit'),
    url(r'rentableDetail/(?P<pk>[0-9]+)/$', views.RentableDetail.as_view(), name='rentableDetail'),
    url(r'store/(?P<pk>[0-9]+)/$', views.StoreDetail.as_view(), name='store'),
    url(r'storeList/$', views.StoreList.as_view(), name='storeList'),
    url(r'rental/(?P<pk>[0-9]+)/$', views.RentalDetail.as_view(), name='rental'),
    url(r'rental/$', views.RentalList.as_view(), name='rentalList'),
    url(r'rented/$', views.Rented.as_view(), name='rented'),
    url(r'rented/(?P<store>[0-9]+)/$', views.Rented.as_view(), name='rentedStore')
    )

