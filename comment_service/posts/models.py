"""Модель Post которая наследует поля Comment"""
from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Поля модели Post"""
    title = models.CharField(max_length=150,
                            verbose_name='Название поста')
    slug = models.SlugField(max_length=150,
                            verbose_name='Слаг поста')
    body = models.TextField(blank=True,
                            verbose_name='Описание поста')
    date_pub = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Время создания поста')


    def get_absolute_url(self):
        """Путь к одному объекту модели Post"""
        return reverse('posts:detail', kwargs={'slug': self.slug})


    # @property
    # def get_comments(self):
    #     return comments.Comment.objects.all()


    def __str__(self):
        """Отображение название объекта"""
        return str(self.title)
