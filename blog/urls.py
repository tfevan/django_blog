from django.conf.urls import url
from . import views

urlpatterns = [
	
	url(r'^$', views.home, name='home'),

	url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),

	url(r'^result/(?P<pk>[0-9]+)/$', views.result, name='result'),


]