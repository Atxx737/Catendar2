# users/signals.py
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
@receiver(post_save, sender=User) #add this
def create_profile(sender, instance, created, **kwargs):
    print('sender',sender)
    print('instance',instance)
    print('created',created)
    if created:
        Profile.objects.create(user=instance)
    
          
@receiver(post_save, sender=User) #add this
def save_profile(sender, instance,  **kwargs):
    instance.profile.save()
# post_save.connect(create_user_profile,sender=User)