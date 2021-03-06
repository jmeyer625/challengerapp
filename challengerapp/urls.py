from django.conf.urls import patterns, url
from challengerapp import views

print ('challengerapp urls')
print views.index

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^challenges/(?P<challenge_id>\d+)/$', views.challenge_detail, name='challenge_detail'),
	url(r'^challenges/$', views.challenge_index, name='challenge_index'),
	url(r'^create-challenge/$', views.create_challenge, name='create_challenge')
)