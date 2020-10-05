from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from polymorphic.models import PolymorphicModel

User = get_user_model()

class Post(PolymorphicModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post', verbose_name='Пользователь')
    title = models.CharField(max_length=150, verbose_name='Название поста')
    slug = models.SlugField(max_length=150, verbose_name='Слаг поста')
    body = models.TextField(blank=True, verbose_name='Описание поста')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Время создания поста')


    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title