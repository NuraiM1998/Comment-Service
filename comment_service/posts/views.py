"""
class PostList, где будет
отображаться список
объектов модели Post

class PostDetail, где будет
отображаться один объект Post,
и список комментариев с вложенностью
и пагинацией
"""
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView, MultipleObjectMixin
from django.views.generic.edit import FormView
from django.http import JsonResponse
from comments.models import Comment, PostComment
from comments.forms import CommentForm
from .models import Post


class PostList(ListView):
    """Список объектов модели Post"""
    model = Post
    template_name = 'post_list.html'


    def get_queryset(self):
        return Post.objects.order_by('date_pub').reverse()


class PostDetail(DetailView, FormView, MultipleObjectMixin):
    """
    один объект Post,
    и список комментариев с вложенностью
    и пагинацией
    """
    model = Post
    template_name = 'post_detail.html'
    form_class = CommentForm
    success_url = reverse_lazy('posts:list')
    paginate_by = 2


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


    def get_context_data(self, **kwargs):
        object_list = PostComment.objects.filter(record_id=self.object)
        context = super().get_context_data(object_list=object_list, **kwargs)
        post = context['object']
        print(post)
        print(context)
        print(dir(post))
        context['comments'] = post.comments.filter(reply__isnull=True) # PostComment.objects.filter(record=post)
        return context


    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
