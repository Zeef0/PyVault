# Generated by Django 4.1.1 on 2022-10-25 03:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=150)),
                ('password', models.CharField(max_length=100, null=True)),
                ('vault_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='vault.vault')),
            ],
            options={
                'verbose_name': 'Informations',
                'verbose_name_plural': 'Informations',
                'db_table': 'vault_Informations',
            },
        ),
    ]
