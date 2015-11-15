from django.conf.urls import url
from . import views 

urlpatterns = [
	#ex: /polls/
	url(r'^$', views.index, name='index'),
	#ex: /polls/5/
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	#ex: /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	#ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),	
	
	#beat_generator ex:rock, jazz
	url(r'^beats/(?P<beat_genre>[a-zA-Z0-9]+)/$', views.beats, name='beats'),
]