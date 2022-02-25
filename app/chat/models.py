from django.db import models

from app.base.models import BaseModel
from django.utils.translation import gettext as _

class Chat(BaseModel):
    user_set = models.ManyToManyField('authentication.User', verbose_name='참여자', blank=True)

    class Meta:
        verbose_name = _('chat')
        verbose_name_plural = verbose_name
        ordering = ['-updated', '-created']

    def get_last_message(self):
        return self.message_set.first()


class MessageSenderTypeChoices(models.TextChoices):
    SENDER = 'S', '발신자'
    RECEIVER = 'R', '수신자'


class Message(BaseModel):
    chat = models.ForeignKey('chat.Chat', verbose_name='채팅', on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.User', verbose_name='유저', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='텍스트', null=True, blank=True)
    image = models.URLField(verbose_name='이미지', null=True, blank=True)

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = verbose_name
        ordering = ['-created']

    def __str__(self):
        return self.text
