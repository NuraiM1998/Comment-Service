'''Testing Comments'''
from datetime import datetime
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from comments.models import Comment, PostComment
from comments.forms import PostCommentForm, CommentForm
from . import factories



class TestCommentModel(TestCase):
    '''Testing Comment model'''
    def setUp(self):
        self.comment = factories.CommentFactory()
        self.comment_reply = factories.PostCommentFactory()
        self.form_data = {
            'user': self.comment_reply.user,
        }
        self.form = PostCommentForm(**self.form_data)


    def test_comment_create_page(self):
        '''Тест наличия страницы comments/<int:post_id>/create/>'''
        response = self.client.get(reverse('comments:create', args=[self.comment.id]))
        # print()
        self.assertTrue(response.context['view'].form_valid(self.form))
        print(dir(response.context['view']))
        self.assertEqual(response.status_code, 200)


    def test_comment_create_reply_page(self):
        '''Тест наличия страницы comments/<int:comment_id>/reply/>'''
        response = self.client.get(reverse('comments:reply', args=[self.comment_reply.id]))
        self.assertTrue(response.context['view'].form_valid(self.form))
        self.assertEqual(response.status_code, 200)


    def test_comment_update_page(self):
        '''Тест наличия страницы comments/<int:pk>/update/>'''
        response = self.client.get(reverse('comments:update', args=[self.comment.id]))
        self.assertEqual(response.status_code, 200)


    def test_comment_delete_page(self):
        '''Тест наличия страницы comments/<int:pk>/delete/>'''
        response = self.client.get(reverse('comments:delete', args=[self.comment.id]))
        self.assertEqual(response.status_code, 200)


    def test_comment_reply_page(self):
        '''Тест наличия страницы comments/<int:comment_id>/reply/>'''
        response = self.client.get(reverse('comments:reply', args=[self.comment.id]))
        self.assertEqual(response.status_code, 200)


    def test_comment_form_is_valid(self):
        form = CommentForm(user=self.comment_reply.user, data=self.form_data)
        self.assertTrue(form.is_valid())
