# Generated by Django 3.1 on 2020-08-20 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20200820_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamplayerstructure',
            name='club',
        ),
    ]
