# Generated by Django 4.2.6 on 2023-10-26 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0011_remove_quiz_sc_ans'),
    ]

    operations = [
        migrations.CreateModel(
            name='s_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]