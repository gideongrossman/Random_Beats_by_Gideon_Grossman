from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django import template
import beat_generator
reload(beat_generator)
import sys
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext



from django.shortcuts import render, get_object_or_404
from .models import Choice, Question, Beat

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
	
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
	
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
	
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a 
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    
def beats(request, beats_in_measure):
    hits, notation = beat_generator.GenerateBeat(beats_in_measure)
    question = Question.objects.get(id=1)
    context = {'beats_in_measure': beats_in_measure, 'hits':hits, 'notation':notation, 'question':question}
    return render(request, 'polls/beats.html', context)

    
def beat_settings(request):
    return render(request, 'polls/beat_settings.html')
    
def sheet_music(request):
    pdf = open('C:\Gideon\Professional Education\djangoTutorialWithoutGal\hellodjango3\polls\static\polls\images\\testFile33.pdf', 'rb')
    response = HttpResponse(pdf.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'filename=some_file.pdf'
    return response
    pdf.closed
    #return render(request, 'polls/sheet_music.html')
    
def beat_saved(request):
    beat_name = request.POST['beat_name']
    beat = Beat(beat_name=beat_name, beat_nickname = "Zip Zop")
    beat.save()
    return HttpResponseRedirect(reverse('polls:beat_index'))
    

def beat_index(request):
    beat_list = Beat.objects.all()
    context = {'beat_list':beat_list}
    return render(request, 'polls/beat_index.html', context)
