from django.db import models
from django.contrib.auth.models import User


class Vault(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return "{}'s Vault".format(self.user_id.username)


class Info(models.Model):
    vault_id = models.ForeignKey(Vault, on_delete=models.CASCADE, related_name="data")
    account = models.CharField(max_length=200)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, blank=True)
    password = models.CharField(max_length=100, null=True)


    class Meta:
        db_table = "vault_Informations"
        verbose_name = "Informations"
        verbose_name_plural = "Informations"
    def __str__(self):
        return self.account 