# Generated by Django 3.0.8 on 2020-10-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_auto_20201006_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistaccount',
            name='Inches',
            field=models.IntegerField(null=True),
        ),
    ]
