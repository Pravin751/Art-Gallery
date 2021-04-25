# Generated by Django 3.0.8 on 2020-09-09 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20200907_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_ids', models.CharField(max_length=250)),
                ('product_ids', models.CharField(max_length=250)),
                ('invoice_id', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=False)),
                ('processed_on', models.DateTimeField(auto_now_add=True)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.register33')),
            ],
        ),
    ]