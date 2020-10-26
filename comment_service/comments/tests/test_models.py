'''Testing Comments'''
from datetime import datetime
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from comments.models import Comment, PostComment
from comments.forms import PostCommentForm, CommentForm
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


def test_comment_reply_page(db, client):
    '''Тест наличия страницы comments/<int:comment_id>/reply/>'''
    comment = factories.CommentFactory()
    response = client.get(reverse('comments:reply', args=[comment.id]))
    assert response.status_code == 200


def test_comment_delete_page(db, client):
    '''Тест наличия страницы comments/<int:pk>/delete/>'''
    comment = factories.CommentFactory()
    response = client.get(reverse('comments:delete', args=[comment.id]))
    assert response.status_code == 200


def test_comment_create_reply_page(db, client):
    '''Тест наличия страницы comments/<int:comment_id>/reply/>'''
    comment_reply = factories.PostCommentFactory()
    response = client.get(reverse('comments:reply', args=[comment_reply.id]))
    assert response.status_code == 200
    # self.assertTrue(response.context['view'].form_valid(self.form))


def test_form_saves_values_to_instance_user_on_save(db):
        comment = factories.CommentFactory()
        comment_user = comment.user
        comment_form = CommentForm(user = comment_user, instance=comment_user, data={'content': 'has_changed'})

        if comment_form.is_valid():
            comment = comment_form.save()
            assert comment_user == comment
        else:
            assert False