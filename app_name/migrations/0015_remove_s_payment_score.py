# Generated by Django 4.2.6 on 2023-10-26 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0014_s_payment_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s_payment',
            name='score',
        ),
    ]
