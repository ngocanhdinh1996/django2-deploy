from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from .models import Profile 


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_profile,sender=User)


def save_profile(sender, instance, **kwarts):
    instance.profile.save()

post_save.connect(save_profile, sender=User)