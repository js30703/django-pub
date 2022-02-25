# Generated by Django 3.2 on 2021-11-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20211115_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_time'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_time'),
        ),
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_time'),
        ),
        migrations.AlterField(
            model_name='message',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_time'),
        ),
    ]
