import factory
from django.contrib.auth.models import User
from comments.models import Comment, PostComment
import datetime
from posts.tests.factories import PostFactory


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'username{0}'.format(n))
    first_name = factory.Sequence(lambda n: 'Nurai{0}'.format(n))
    last_name = factory.Sequence(lambda n: 'Maratova{0}'.format(n))
    email = factory.Sequence(lambda n: 'email{0}@gmail.com'.format(n))


class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment

    user = factory.SubFactory(UserFactory)
    content = factory.Faker('name')
    timestamp = factory.LazyFunction(datetime.datetime.now)


class PostCommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = PostComment

    user = factory.SubFactory(UserFactory)
    record = factory.SubFactory(PostFactory)
    