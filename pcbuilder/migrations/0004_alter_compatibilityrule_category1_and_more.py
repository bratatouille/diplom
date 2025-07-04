# Generated by Django 5.2 on 2025-06-20 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcbuilder', '0003_alter_categorypc_options_and_more'),
        ('store', '0008_remove_userpromocode_email_promocode_is_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compatibilityrule',
            name='category1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compat_rules_1', to='store.category', verbose_name='Категория 1'),
        ),
        migrations.AlterField(
            model_name='compatibilityrule',
            name='category2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compat_rules_2', to='store.category', verbose_name='Категория 2'),
        ),
        migrations.AlterField(
            model_name='compatibilityrule',
            name='error_message',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Сообщение об ошибке'),
        ),
        migrations.AlterField(
            model_name='compatibilityrule',
            name='operator',
            field=models.CharField(blank=True, choices=[('=', 'Равно'), ('!=', 'Не равно'), ('<', 'Меньше'), ('<=', 'Меньше или равно'), ('>', 'Больше'), ('>=', 'Больше или равно')], max_length=2, null=True, verbose_name='Оператор'),
        ),
        migrations.AlterField(
            model_name='compatibilityrule',
            name='spec1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compat_rules_1', to='store.specification', verbose_name='Характеристика 1'),
        ),
        migrations.AlterField(
            model_name='compatibilityrule',
            name='spec2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compat_rules_2', to='store.specification', verbose_name='Характеристика 2'),
        ),
    ]
