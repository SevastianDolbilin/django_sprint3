# Generated by Django 3.2.16 on 2024-07-25 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['created_at']},
        ),
    ]
