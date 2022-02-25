# Generated by Django 3.2 on 2021-12-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_alter_patient_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='last_scaling_date',
            field=models.DateField(blank=True, null=True, verbose_name='last scaling date'),
        ),
        migrations.AddField(
            model_name='patient',
            name='last_visit_date',
            field=models.DateField(blank=True, null=True, verbose_name='last visit date'),
        ),
    ]
