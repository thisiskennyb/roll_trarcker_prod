# Generated by Django 4.2.5 on 2023-10-17 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_dollar_value_searched'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='coin_collection',
        ),
    ]
