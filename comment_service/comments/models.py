from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from polymorphic.models import PolymorphicModel


User = get_user_model()


class Comment(PolymorphicModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post', verbose_name='Пользователь')
    content = models.TextField(verbose_name='Контент')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    reply = models.ForeignKey('self', null=True, on_delete=models.PROTECT, related_name='replies', verbose_name='Ответ на комментарий')
    

    class Meta:
        ordering = ['-timestamp']


    def __str__(self):
        return f"{self.user.username}'s comment"