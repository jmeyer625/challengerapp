from django.conf.urls import patterns, include, url
from django.contrib import admin
import challengerapp.views

urlpatterns = patterns('',
	url(r'^$', challengerapp.views.index, name='index'),
    url(r'^challengerapp/', include('challengerapp.urls',namespace='challengerapp')),
    url(r'^admin/', include(admin.site.urls)),
)