# Generated by Django 3.2 on 2021-11-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0003_auto_20211116_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(choices=[('CR', 'Created'), ('TR', 'Treated'), ('PA', 'Paid')], default='CR', max_length=50),
        ),
    ]
