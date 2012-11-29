from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    #this fiedl is required
    user = models.OneToOneField(User)
    
    #additional field
    accepted_eula = models.BooleanField()
    hobby = models.CharField(max_length=100)
    favorite_animal = models.CharField(max_length=100)