# Generated by Django 3.0.8 on 2020-09-18 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_remove_register33_emailid'),
    ]

    operations = [
        migrations.AddField(
            model_name='register33',
            name='emailid',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
