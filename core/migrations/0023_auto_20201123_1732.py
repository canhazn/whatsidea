# Generated by Django 3.0.11 on 2020-11-23 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_merge_20201123_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idea',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='idea',
            name='problem',
            field=models.TextField(blank=True),
        ),
    ]