# Generated by Django 3.0.8 on 2020-10-11 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0054_auto_20201012_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customphoto',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.register33'),
        ),
    ]
