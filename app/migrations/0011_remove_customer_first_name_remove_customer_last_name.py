# Generated by Django 5.0.7 on 2024-07-16 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_name_customer_first_name_customer_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]
