from django.db import models
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True
# Create your models here.

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   bio = models.CharField(max_length=200, blank=True)
