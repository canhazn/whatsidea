# Generated by Django 3.0.11 on 2020-11-18 10:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0017_auto_20201118_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='user',
        ),
        migrations.AddField(
            model_name='idea',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]