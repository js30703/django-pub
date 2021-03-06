# Generated by Django 3.2 on 2021-11-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icf001',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_time'),
        ),
        migrations.AlterField(
            model_name='icf001',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_time'),
        ),
        migrations.AlterField(
            model_name='icf002',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_time'),
        ),
        migrations.AlterField(
            model_name='icf002',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_time'),
        ),
        migrations.AlterField(
            model_name='ifc001_2',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_time'),
        ),
        migrations.AlterField(
            model_name='ifc001_2',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_time'),
        ),
    ]
