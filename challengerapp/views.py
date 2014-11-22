from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from challengerapp.models import Challenge
# Create your views here.

def index(request):
	return HttpResponse('Hello, world!')

def challenge_detail(request, challenge_id):
	challenge = get_object_or_404(Challenge,pk=challenge_id)
	return HttpResponse("You're looking at the page for %s." % challenge.title)

def challenge_index(request):
	challenges = Challenge.objects.all()
	context = {'challenges': challenges}
	return render(request, 'challengerapp/index.html', context)