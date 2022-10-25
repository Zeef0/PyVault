from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Vault


@receiver(post_save, sender=User)
def create_vault(sender, instance, created, **kwargs):
    if created:
        print(sender, instance, created)
        print(kwargs)
        Vault.objects.create(user_id=instance)
