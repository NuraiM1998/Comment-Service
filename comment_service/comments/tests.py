from .models import Comment, Post
from datetime import datetime
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()

class TestPostModel(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='test_user', password='test12345')
        self.title = 'Test Title'
        self.slug = 'test-slug'
        self.body = 'Test Body'
        self.date_pub = datetime.now()
        self.test_post = Post.objects.create(user=user, title=self.title, slug=self.slug, body=self.body, date_pub=self.date_pub)

    def test_post_detail_page(self):
        # response = self.client.get('blog/posts/'+str(self.test_post.slug)+'/')
        response = self.client.get(reverse('comments:post_detail', args=[self.test_post.slug]))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, self.test_post.title)

class TestCommentModel(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='test_user', password='test12345')
        self.content = 'Test Content'
        self.timestamp = datetime.now()
        self.test_comment = Comment(user=user, content=self.content, timestamp=self.timestamp)
        
    # def test_comment_page(self):
    #     response = self.client.get(reverse('comments:post_detail', args=[self.test_post.slug]))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertContains(response, self.test_comment.content)