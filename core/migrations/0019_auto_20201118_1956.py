# Generated by Django 3.0.11 on 2020-11-18 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20201118_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='user',
            new_name='founder',
        ),
    ]