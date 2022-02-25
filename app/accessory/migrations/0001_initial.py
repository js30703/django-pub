# Generated by Django 3.2 on 2021-12-12 10:57

from django.db import migrations, models
import django.db.models.deletion
import utills.uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', utills.uuid.CustomUUIDField(blank=True, editable=False, max_length=10, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('stock', models.PositiveIntegerField(verbose_name='stock')),
            ],
            options={
                'verbose_name': 'Accessory',
                'verbose_name_plural': 'Accessory',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', utills.uuid.CustomUUIDField(blank=True, editable=False, max_length=10, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('phone', models.CharField(max_length=50, verbose_name='phone')),
                ('memo', models.TextField(blank=True, verbose_name='memo')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated_time')),
                ('uuid', utills.uuid.CustomUUIDField(blank=True, editable=False, max_length=10, unique=True)),
                ('num', models.PositiveIntegerField(verbose_name='number')),
                ('cost', models.PositiveIntegerField(verbose_name='cost')),
                ('price', models.PositiveIntegerField(verbose_name='pirce')),
                ('accessory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accessory.accessory', verbose_name='accessory')),
            ],
            options={
                'verbose_name': 'Sales',
                'verbose_name_plural': 'Sales',
            },
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated_time')),
                ('uuid', utills.uuid.CustomUUIDField(blank=True, editable=False, max_length=10, unique=True)),
                ('num', models.PositiveIntegerField(verbose_name='number')),
                ('cost', models.PositiveIntegerField(verbose_name='cost')),
                ('accessory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accessory.accessory', verbose_name='accessory')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accessory.supplier', verbose_name='accessory')),
            ],
            options={
                'verbose_name': 'Procurement',
                'verbose_name_plural': 'Procurement',
            },
        ),
    ]