# Generated by Django 3.0.8 on 2020-09-06 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_artistaccount_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_on', models.DateTimeField(auto_now=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ArtistAccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.register33')),
            ],
        ),
    ]
