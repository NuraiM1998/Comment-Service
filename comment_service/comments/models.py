"""
Модель Comment
от которой будут
наследовать поля
другие модели
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from polymorphic.models import PolymorphicModel
from posts.models import Post
from comments.closure import ClosureModel


class Comment(PolymorphicModel):
    """Поля модели Comment"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_post',
        verbose_name='Пользователь'
    )
    content = models.TextField(verbose_name='Контент')
    timestamp = models.DateTimeField(auto_now_add=True, 
                                    verbose_name='Время создания')
    parent = models.ForeignKey('self',
                            null=True,
                            on_delete=models.PROTECT,
                            related_name='replies',
                            verbose_name='Ответ на комментарий',
                            blank=True)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        """Отображаются самые новые комментарии"""
        ordering = ['-timestamp']



class CommentHierarchy(models.Model):
    parent = models.ForeignKey(Comment, 
                        on_delete=models.SET_NULL, 
                        related_name='children', 
                        null=True)
    child = models.ForeignKey(Comment, 
                        on_delete=models.SET_NULL, 
                        related_name='parents', 
                        null=True)
    depth = models.IntegerField(default=0)


class PostComment(Comment):
    """Комменты которые относятся к посту"""
    record = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content

    def depth(self):
        print(self.parents.all())
        return self.parents.filter(depth__gt=0).last()


class Node(ClosureModel): # пока что не используется(возможно в будущем уберу)
    user = models.ForeignKey(User, 
                    on_delete=models.CASCADE, 
                    related_name='user_nodes', 
                    null=True, 
                    verbose_name='Пользователь')
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', 
                            on_delete=models.CASCADE, 
                            related_name='children', 
                            null=True, 
                            blank=True)
    post = models.ForeignKey(Post, 
                            on_delete=models.CASCADE, 
                            related_name='nodes', 
                            null=True)


# @receiver(post_save, sender=PostComment)
# def save_hierarchy(sender, instance=None, created=False, **kwargs):
#     print('instance: ', instance)
#     print('instance.parent: ',instance.parent)
#     # print('instance.child: ',instance.child)
#     if created:
#         self_comment = CommentHierarchy.objects.create( # текущий коммент
#                                         parent=instance,
#                                         child=instance)
#         if instance.parent: # если у комента есть родитель
#             parent_hierarchy = CommentHierarchy.objects.filter( # фильтруем родителей которые не вложенны(root)
#                                                     child=instance.parent,
#                                                     depth__gt=0)
#             CommentHierarchy.objects.create(parent=instance.parent,
#                                             child=instance,
#                                             depth=1)
#             for node in parent_hierarchy:
#                 CommentHierarchy.objects.create(
#                                     parent=node.parent,
#                                     child=instance,
#                                     depth=node.depth+1)
#                 print('node: ', node)
#                 print('node.parent: ', node.parent)
