# Generated by Django 4.2.5 on 2023-10-05 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0010_quiz_sc_ans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='sc_ans',
        ),
    ]
