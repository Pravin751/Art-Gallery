# Generated by Django 3.0.8 on 2020-08-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_artistaccount_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistaccount',
            name='image',
            field=models.FileField(null=True, upload_to='media/post/'),
        ),
    ]
