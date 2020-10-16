import datetime
import factory
from posts.models import Post


class PostFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Post

    title = factory.Iterator(['Post Title 1', 'Post Title 2', 'Post Title 3', 'Post Title 4'])
    slug = factory.Iterator(['post-title-1', 'post-title-2', 'post-title-3', 'post-title-4'])
    body = factory.Iterator(['Post Body 1', 'Post Body 2', 'Post Body 3', 'Post Body 4'])
    date_pub = factory.LazyFunction(datetime.datetime.now)
