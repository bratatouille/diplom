# Generated by Django 5.2 on 2025-06-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_promocode_is_personal_userpromocode_is_personal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpromocode',
            name='is_personal',
        ),
        migrations.AddField(
            model_name='userpromocode',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
    ]
