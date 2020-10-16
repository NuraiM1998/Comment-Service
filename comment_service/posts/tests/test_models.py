'''Testing Post Model'''
from django.urls import reverse
from django.test import TestCase
from . import factories


class TestPostModel(TestCase):
    '''Testing Post model'''


    def test_post_detail_page(self):
        '''Тест на наличие страницы comments/<slug:slug>/ и контента в ней'''
        post = factories.PostFactory()
        response = self.client.get(reverse('posts:detail', args=[post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
