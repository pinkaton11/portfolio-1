# Generated by Django 2.0.2 on 2018-09-28 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20180929_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitemheader',
            name='item_type',
        ),
        migrations.RemoveField(
            model_name='menuitemheader',
            name='url',
        ),
    ]