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
	url(r'^beats/(?P<beats_in_measure>[0-9]+)/$', views.beats, name='beats'),
	url(r'^beats/$', views.beat_settings, name = 'beat_settings'),
	url(r'^beats/sheet_music/$', views.sheet_music, name = 'sheet_music'),
	url(r'^beats/beat_saved/$', views.beat_saved, name = 'beat_saved'),
	url(r'^beats/beat_index/$', views.beat_index, name = 'beat_index'),
	url(r'^beats/beat_detail/(?P<beat_id>[0-9]+)/$', views.beat_detail, name = 'beat_detail'),
	url(r'^beats/delete_beat/(?P<beat_id>[0-9]+)/$', views.delete_beat, name = 'delete_beat'),
	url(r'^beats/delete_all_beats/$', views.delete_all_beats, name = 'delete_all_beats'),
	url(r'^beats/create_a_pdf/$', views.pdf_generating_view, name = 'pdf_generator'),
	url(r'^beats/beat_pdf_saved/$', views.upload_file, name = 'file_upload'),
]