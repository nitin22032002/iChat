# Generated by Django 3.2.4 on 2021-11-14 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatRoom', '0006_remove_room_room_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='signup_status',
        ),
    ]
