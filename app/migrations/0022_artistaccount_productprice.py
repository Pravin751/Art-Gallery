# Generated by Django 3.0.8 on 2020-09-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistaccount',
            name='productprice',
            field=models.FloatField(null=True),
        ),
    ]
