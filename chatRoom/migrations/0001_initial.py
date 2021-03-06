# Generated by Django 3.2.4 on 2021-11-13 02:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('sender_id', models.IntegerField()),
                ('message', models.CharField(max_length=1000000000)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 11, 13, 8, 18, 16, 705418))),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('signup_status', models.BooleanField(default=False)),
                ('block_status', models.BooleanField(verbose_name=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_id', models.IntegerField()),
                ('date_start', models.DateTimeField(default=datetime.datetime(2021, 11, 13, 8, 18, 16, 705418))),
                ('date_end', models.DateTimeField(default=datetime.datetime(2021, 11, 13, 8, 18, 16, 705418))),
            ],
        ),
    ]
