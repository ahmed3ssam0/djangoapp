# Generated by Django 5.0.7 on 2024-07-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_customer_first_name_remove_customer_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
