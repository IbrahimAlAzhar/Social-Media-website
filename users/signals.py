from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
# the reason of this file is each time when a new user's registration complete then default picture is already set up


@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):  # the parameters which one pass from receiver
    if created:      # if the profile is created then create the profile object
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)  # inherit by receiver
def save_profile(sender, instance,**kwargs):  # kwargs send the additional elements
    instance.profile.save()


