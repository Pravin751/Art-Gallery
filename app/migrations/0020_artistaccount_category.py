# Generated by Django 3.0.8 on 2020-09-05 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_artistaccount_productname'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistaccount',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
    ]
