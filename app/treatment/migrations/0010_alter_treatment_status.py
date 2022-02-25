# Generated by Django 3.2 on 2021-12-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0009_alter_treatment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('Treated', 'Treated'), ('Paid', 'Paid')], default='Created', max_length=50),
        ),
    ]