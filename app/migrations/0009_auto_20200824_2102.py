# Generated by Django 3.0.8 on 2020-08-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_artistaccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistaccount',
            name='date',
        ),
        migrations.AddField(
            model_name='artistaccount',
            name='content',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
