# Generated by Django 3.0.8 on 2020-08-01 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200729_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='register33',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='register33',
            name='username',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]