from django.shortcuts import render
from django.http import HttpResponse
from challengerapp.models import Challenge
# Create your views here.

def index(request):
	return HttpResponse('Hello, world!')

def challenge_detail(request, challenge_id):
	return HttpResponse("You're looking at the page for %s." % challenge_id)

def challenge_index(request):
	challenges = Challenge.objects.all()
	output = ','.join(c.title for c in challenges)
	return HttpResponse(output)