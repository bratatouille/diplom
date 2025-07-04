# Generated by Django 5.2.1 on 2025-06-15 09:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('schedule', models.CharField(max_length=100, verbose_name='Режим работы')),
                ('map_link', models.URLField(blank=True, max_length=500, verbose_name='Ссылка на карту')),
            ],
            options={
                'verbose_name': 'Контактная информация',
                'verbose_name_plural': 'Контактная информация',
            },
        ),
        migrations.AlterModelOptions(
            name='heroslide',
            options={'ordering': ['order'], 'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайды'},
        ),
        migrations.RenameField(
            model_name='heroslide',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RemoveField(
            model_name='heroslide',
            name='button1_text',
        ),
        migrations.RemoveField(
            model_name='heroslide',
            name='button1_url',
        ),
        migrations.RemoveField(
            model_name='heroslide',
            name='button2_text',
        ),
        migrations.RemoveField(
            model_name='heroslide',
            name='button2_url',
        ),
        migrations.AddField(
            model_name='heroslide',
            name='link',
            field=models.URLField(blank=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='heroslide',
            name='image',
            field=models.ImageField(upload_to='hero_slides/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='heroslide',
            name='subtitle',
            field=models.CharField(max_length=300, verbose_name='Подзаголовок'),
        ),
        migrations.CreateModel(
            name='SupportTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('topic', models.CharField(max_length=100, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В обработке'), ('closed', 'Закрыта')], default='new', max_length=20, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заявка в поддержку',
                'verbose_name_plural': 'Заявки в поддержку',
                'ordering': ['-created_at'],
            },
        ),
    ]
