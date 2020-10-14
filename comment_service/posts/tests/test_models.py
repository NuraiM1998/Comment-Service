'''Testing Post Model'''
from datetime import datetime
from django.urls import reverse
from django.test import TestCase
from posts.models import Post


class TestPostModel(TestCase):
    '''Testing Post model'''
    def setUp(self):
        self.title = 'Test Title'
        self.slug = 'test-slug'
        self.body = 'Test Body'
        self.date_pub = datetime.now()
        self.test_post = Post.objects.create(
                            title=self.title,
                            slug=self.slug,
                            body=self.body,
                            date_pub=self.date_pub
                            )

    def test_post_detail_page(self):
        '''Тест наличия страницы comments/<slug:slug>/'''
        response = self.client.get(reverse('posts:detail', args=[self.test_post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.test_post.title)
