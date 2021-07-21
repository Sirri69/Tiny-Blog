from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

def index(request):
	return HttpResponse('<h1>Hello<h1/>')

def check_username(request):
	#GARBAGE CODE, TO BE OPTIMIZED LATER
	uname = str(request.GET.get('uname')).lower()
	# return HttpResponse(uname)

	# if list(User.objects.all().filter(username = uname)) == []:	
	if User.objects.filter(username = uname).first() is None:
		return HttpResponse('OK')
	else:
		if User.objects.all().filter(username = uname).first().is_active:
			return HttpResponse('Not-OK')
		else:
			User.objects.all().filter(username = uname).first().delete()

			return HttpResponse('OK')


	# return HttpResponse('checking')


def check_email(request):
	#GARBAGE CODE, TO BE OPTIMIZED LATER
	email = str(request.GET.get('mail')).lower()

	if User.objects.all().filter(email = email).first() is None :	
		return HttpResponse('OK')
	else:
		if User.objects.all().filter(email = email).first().is_active:
			return HttpResponse('Not-OK')
		else:
			User.objects.all().filter(email = email).first().delete()
			return HttpResponse('OK')


