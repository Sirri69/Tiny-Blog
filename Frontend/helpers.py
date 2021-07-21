from cryptography import fernet
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
import time
import uuid


def send_email_confirmation(recipent_uname,recipent_mail):

	'''
	Sends a link to connfirm email and activate user
	'''

	f = fernet.Fernet(settings.CRYPT_KEY)
	enc = f.encrypt_at_time(bytes(str(recipent_uname), encoding='UTF-8'), current_time=int(time.time()))
	send_mail(
	    'Confrim your email',
	    None,
	    'Documentorblog@gmail.com',
	    [recipent_mail],
	    html_message = loader.render_to_string('frontend/email_templates/email_confirmation.html',
	    	{
	    	'user_email' : str(recipent_mail),
	    	'enc':enc.decode()
	    	}),
	    fail_silently=False,
	)

def send_reset_link(recipent_mail):
	'''
	Sends a password reset link to recipent_mail
	'''
	f = fernet.Fernet(settings.CRYPT_KEY)
	enc = f.encrypt_at_time(bytes(str(recipent_mail), encoding='UTF-8'), current_time=int(time.time()))
	send_mail(
	    'Reset your password',
	    f'Please click on this link: http://127.0.0.1:8080/reset_password/{enc.decode()} to reset your password. Link only valid for 2 hours.',
	    'Documentorblog@gmail.com',
	    [recipent_mail],
	    fail_silently=False,
	)
	print('Mail-Sent')


def generate_password():
	password = uuid.uuid4()
	return str(password)
