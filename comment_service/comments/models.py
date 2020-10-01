from .forms import CommentForm
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey




User = get_user_model()

class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    body = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)



    def get_absolute_url(self):
        return reverse('comments:post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs


    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type.model


class Comment(models.Model):
    objects = CommentManager()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # post = models.ForeignKey(Post, on_delete=models.PROTECT)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-timestamp']


    def __str__(self):
        return f"{self.user.username}'s comment"

    def children(self): #replies
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True