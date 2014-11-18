from django.conf.urls import patterns, url
from challengerapp import views

print ('challengerapp urls')
print views.index

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^(?P<challenge_id>\d+)/$', views.challenge_detail, name='detail'),
	url(r'^challenges$', views.challenge_index, name='challenge_index')
)