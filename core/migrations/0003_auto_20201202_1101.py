# Generated by Django 3.0.11 on 2020-12-02 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Comment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Post'),
        ),
    ]
