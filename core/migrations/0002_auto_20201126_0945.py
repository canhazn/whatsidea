# Generated by Django 3.0.11 on 2020-11-26 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='description',
            field=models.TextField(default='Have no Idea!'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='solution',
            field=models.TextField(blank=True),
        ),
    ]
