from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Documentor.models import Profile
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.conf import settings
from cryptography import fernet
from .helpers import send_email_confirmation, send_reset_link, generate_password
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
		return redirect('/profile')
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
		return redirect('/profile')
	isLoggedIn = 'true'
	if request.method == "GET":
		return render(request, "frontend/login.html", context={'isLoggedIn':isLoggedIn})
	if request.method == "POST":
		uname = request.POST.get('uname').lower()
		password = request.POST.get('passwd')
		remember_me = request.POST.get('remember_me')
		user = authenticate(username=uname, password=password)
		print(password)
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


def password_reset(request, enc='def'):
	if request.method == 'POST':
		mail = request.POST.get('mail', None)
		send_reset_link(mail)
		return redirect('/login')

	elif request.method == 'GET':
		if enc == 'def':
			return HttpResponse('Some error occured')
		else:
			f = fernet.Fernet(settings.CRYPT_KEY)
			dec = f.decrypt_at_time(bytes(enc, encoding='UTF-8'), ttl=7200, current_time=int(time.time())).decode()
			password = generate_password()
			usr = User.objects.filter(email = dec).first()
			if usr is None: return HttpResponse('Sorry, your email is not registered in our database')
			usr.password = make_password(password)
			usr.save()
			return HttpResponse(f'''We have changed your password to {password}, you can change it in settings.
			 <br> Please click <a href="http://127.0.0.1:8080/login">here</a> to login. Please remember this password,
			  you will need it to reset it.''')





def home(request):
	return render(request, 'frontend/home.html')
	# return HttpResponse('App')

def confirm_email(request,enc):
	f = fernet.Fernet(settings.CRYPT_KEY)
	dec = f.decrypt_at_time(bytes(enc, encoding='UTF-8'), ttl=7200, current_time=int(time.time())).decode()
	usr = User.objects.get(username=dec)
	usr.is_active = True
	usr.save()
	return redirect(profile)
