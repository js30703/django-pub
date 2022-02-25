# Generated by Django 3.2 on 2021-11-12 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('user_set', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='참여자')),
            ],
            options={
                'verbose_name': '채팅',
                'verbose_name_plural': '채팅',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('text', models.TextField(blank=True, null=True, verbose_name='텍스트')),
                ('image', models.URLField(blank=True, null=True, verbose_name='이미지')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chat', verbose_name='채팅')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': '메세지',
                'verbose_name_plural': '메세지',
                'ordering': ['-created'],
            },
        ),
    ]
