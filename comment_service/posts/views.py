from django.shortcuts import render, get_object_or_404
from .models import Post
from comments.forms import CommentCreateForm
from datetime import datetime
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    

    def get_queryset(self):
        return Post.objects.order_by('date_pub').reverse()


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    queryset = Post.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = CommentCreateForm()
        context['comment_form'] = comment_form
        return context


class CommentCreate(CreateView):
    model = Comment
    form_class = CommentCreateForm