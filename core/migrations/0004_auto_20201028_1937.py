# Generated by Django 3.1.2 on 2020-10-28 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_idea_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='username',
            new_name='slug',
        ),
    ]
