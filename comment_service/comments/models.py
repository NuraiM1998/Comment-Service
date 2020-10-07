"""
Модель Comment
от которой будут
наследовать поля
другие модели
"""
from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel


class Comment(PolymorphicModel):
    """Поля модели Comment"""
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='user_post',
                            verbose_name='Пользователь')
    content = models.TextField(verbose_name='Контент')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    reply = models.ForeignKey('self',
                            null=True,
                            on_delete=models.PROTECT,
                            related_name='replies',
                            verbose_name='Ответ на комментарий')


    class Meta:
        """Отображаются самые новые комментарии"""
        ordering = ['-timestamp']


    def __str__(self):
        return f"{self.user}'s comment"
