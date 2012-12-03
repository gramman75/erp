from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class UserProfile(models.Model):
    #this fiedl is required
    user = models.OneToOneField(User)
    
    #additional field
    accepted_eula = models.BooleanField()
    hobby = models.CharField(max_length=100)
    favorite_animal = models.CharField(max_length=100)
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)