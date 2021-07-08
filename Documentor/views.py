from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

def index(request):
	return HttpResponse('<h1>Hello<h1/>')

def check_username(request):
	uname = str(request.GET.get('uname'))#.lower()
	# return HttpResponse(uname)

	if list(User.objects.all().filter(username = uname)) == []:	
		return HttpResponse('OK')
	else:
		return HttpResponse('Not-OK')
	# return HttpResponse('checking')