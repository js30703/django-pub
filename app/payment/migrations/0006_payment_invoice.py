# Generated by Django 3.2 on 2021-12-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_payment_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='invoice',
            field=models.FileField(null=True, upload_to='payment/', verbose_name='invoice'),
        ),
    ]
