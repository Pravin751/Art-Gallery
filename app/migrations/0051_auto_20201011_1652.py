# Generated by Django 3.0.8 on 2020-10-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0050_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(null=True, upload_to='img/'),
        ),
    ]
