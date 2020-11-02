'''Testing Comments'''
from datetime import datetime
from django.urls import reverse
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from copy import deepcopy
from comments.models import Comment, PostComment
from comments.forms import PostCommentForm, CommentForm
from comments.views import PostCommentView
from faker import Faker
from . import factories
import pytest


@pytest.mark.parametrize(
    'user, content, validity',
    [('me@mail.ru', 'Some content',  True),
     ('me5@mail.ru', '',  False),
     (None, None, False),
     ])
def test_example_form(db, user, content, validity):
    comment = factories.CommentFactory()
    comment_user = comment.user
    form = CommentForm(user=comment_user, data={
        'user': user,         
        'content': content,
    })

    assert form.is_valid() is validity


def test_comment_update_page(db, client):
    '''Тест наличия страницы comments/<int:pk>/update/>'''
    comment = factories.CommentFactory()
    response = client.get(reverse('comments:update', args=[comment.id]))
    assert response.status_code == 200


def test_comment_delete_page(db, client):
    '''Тест наличия страницы comments/<int:pk>/delete/>'''
    comment = factories.CommentFactory()
    response = client.get(reverse('comments:delete', args=[comment.id]))
    print('Response', dir(response.context))
    print('Response', response.context)
    assert response.status_code == 200


def test_form_saves_values_to_instance_user_on_save(db, client):
    comment = factories.CommentFactory()
    comment_user = comment.user
    comment_form = CommentForm(user = comment_user, instance=comment_user, data={'content': 'has_changed'})

    if comment_form.is_valid():
        comment = comment_form.save()
        assert comment_user == comment
    else:
        assert False


def test_signal_save_hierarchy(db, client):
    '''Проверка сигнала который 
    создает записи в связующей
    '''
    def save_hierarchy(form_data, **kwargs):
        content = form_data['content']
        form_data = {
            'content': 'Some content'
        }

        signals.save_hierarchy.connect(save_hierarchy, sender='test', form_data=form_data)
        assert content, 'Some content'
        

def test_str_is_equal_to_content(db, client):
    """
    Method `__str__` should be equal to field `content`
    """
    post_comment = factories.PostCommentFactory()
    assert str(post_comment) == post_comment.content


fake = Faker()
PASSWORD = fake.password()


@pytest.fixture()
def user(db):
    return factories.UserFactory.create(password=make_password(PASSWORD))


@pytest.fixture()
def auth_client(client, user):
    client = deepcopy(client)
    client.login(username=user.username, password=PASSWORD)
    return client


@pytest.mark.usefixtures("auth_client")
def test_get_form_kwargs(db, auth_client):
    response = auth_client.get(reverse('comments:create_com'))
    assert 'user' in response.context['view'].get_form_kwargs()
