'''Testing Comments'''
from datetime import datetime
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comment


class TestCommentModel(TestCase):
    '''Testing Comment model'''
    def setUp(self):
        user = User.objects.create_user(
                    username='test_user',
                    password='test12345'
                    )
        self.content = 'Test Content'
        self.timestamp = datetime.now()
        self.reply = 'Reply Test'
        self.test_comment = Comment.objects.create(
                                user=user,
                                content=self.content,
                                timestamp=self.timestamp
                                )


    def test_comment_create_page(self):
        '''Тест наличия страницы comments/<int:post_id>/create/>'''
        response = self.client.get(reverse('comments:create', args=[self.test_comment.id]))
        self.assertEqual(response.status_code, 200)


    def test_comment_update_page(self):
        '''Тест наличия страницы comments/<int:pk>/update/>'''
        response = self.client.get(reverse('comments:update', args=[self.test_comment.id]))
        self.assertEqual(response.status_code, 200)


    def test_comment_delete_page(self):
        '''Тест наличия страницы comments/<int:pk>/delete/>'''
        response = self.client.get(reverse('comments:delete', args=[self.test_comment.id]))
        self.assertEqual(response.status_code, 200)


    def test_comment_reply_page(self):
        '''Тест наличия страницы comments/<int:comment_id>/reply/>'''
        response = self.client.get(reverse('comments:reply', args=[self.test_comment.id]))
        self.assertEqual(response.status_code, 200)
