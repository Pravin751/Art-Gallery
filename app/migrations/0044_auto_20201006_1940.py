# Generated by Django 3.0.8 on 2020-10-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_category_cover_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='register33',
            name='Address',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='register33',
            name='contact_number',
            field=models.IntegerField(null=True),
        ),
    ]
