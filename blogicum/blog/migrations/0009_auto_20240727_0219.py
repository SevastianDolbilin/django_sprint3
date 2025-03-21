# Generated by Django 3.2.16 on 2024-07-27 00:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20240726_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Снимите галочку, чтобы скрыть публикацию.', verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Если установить дату и время в будущем — можно делать отложенные публикации.', verbose_name='Дата и время публикации'),
        ),
    ]
