from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Documentor.models import Profile
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.template import loader
from cryptography import fernet
import time

# Create your views here.

def index(request):
	user = None
	if request.user.is_authenticated:
		user = request.user
		
	isLoggedIn = 'true' if user else 'false'
	return render(request, 'frontend/index.html',context={'isLoggedIn':isLoggedIn})

def signup(request):
	isLoggedIn = 'false'
	if request.user.is_authenticated:
		redirect(app)
	return render(request, 'frontend/signup.html',context={'isLoggedIn':isLoggedIn})

def register(request):
	if request.method == "POST":
		email = request.POST.get('email')
		uname = (request.POST.get('uname')).lower()
		password = make_password(request.POST.get('pass1'))	
		f_name = request.POST.get('f_name')
		l_name = request.POST.get('l_name')
		usr = User(username=uname, password=password,
			 first_name=f_name, last_name=l_name, email=email, is_active=False)
		usr.save()
		u = Profile(user=usr, bio='')
		send_email_confirmation(recipent_uname=uname, recipent_mail=email)
		u.save()
		
	return render(request,'frontend/confirm_email.html')

def login_user(request):
	if request.user.is_authenticated :
		redirect(index)
	isLoggedIn = 'true'
	if request.method == "GET":
		return render(request, "frontend/login.html", context={'isLoggedIn':isLoggedIn})
	if request.method == "POST":
		uname = request.POST.get('uname')
		password = request.POST.get('passwd')
		remember_me = request.POST.get('remember_me')
		user = authenticate(username=uname, password=password)
		if user is not None:
			login(request, user)
			if remember_me == 'on':
				request.session.set_expiry(settings.SESSION_LENGTH)
			else:
				request.session.set_expiry(0)
			return redirect(profile)
		else:
			return HttpResponse("Login User or Password incorrect")

@login_required
def profile(request):
	if request.user.is_authenticated:
		user = request.user
		isLoggedIn = 'true' if user else 'false'
		# return HttpResponse(f"Id:- {user.id}, First Name:- {user.first_name} Bio:- {user.profile.bio}")
		return render(request, 'frontend/profile.html',context={'uname':user.username,
																'bio':user.profile.bio,
																'fname':user.first_name,
																'isLoggedIn':isLoggedIn,
																'isActive':user.is_active})
	else:
		return HttpResponse("Not authenticated")


def app(request):
	return HttpResponse('App')

def send_email_confirmation(recipent_uname,recipent_mail):
	f = fernet.Fernet(settings.CRYPT_KEY)
	enc = f.encrypt_at_time(bytes(str(recipent_uname), encoding='UTF-8'), current_time=int(time.time()))
	send_mail(
	    'Confrim your email',
	    None,
	    'Documentorblog@gmail.com',
	    [recipent_mail],
	    html_message = loader.render_to_string('frontend/email_templates/email_confirmation.html',
	    	{
	    	'user_email' : 'pranav2278@gmail.com',
	    	'enc':enc.decode()
	    	}),
	    fail_silently=False,
	)
	return HttpResponse('Done')

def confirm_email(request,enc):
	f = fernet.Fernet(settings.CRYPT_KEY)
	dec = f.decrypt_at_time(bytes(enc, encoding='UTF-8'), ttl=7200, current_time=int(time.time())).decode()
	print(dec)
	usr = User.objects.get(username=dec)
	usr.is_active = True
	usr.save()
	return redirect(profile)

