# Generated by Django 3.0.11 on 2020-12-04 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201202_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='contribution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Contribution'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='idea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Idea'),
        ),
    ]
