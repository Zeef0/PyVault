from django.test import TestCase
from django.contrib.auth.models import User

class Vault(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.CharField(max_length=150)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
