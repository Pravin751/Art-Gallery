# Generated by Django 3.0.8 on 2020-08-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200801_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='register33',
            name='picture',
            field=models.FileField(null=True, upload_to='post/'),
        ),
    ]
