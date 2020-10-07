from .models import Post
from comments.models import Comment
from datetime import datetime
from .forms import CommentForm
from django.http import Http404
from django.utils import timezone
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView, MultipleObjectMixin
from django.views.generic.edit import CreateView, FormView, FormMixin


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'


    def get_queryset(self):
        return Post.objects.order_by('date_pub').reverse()


class PostDetail(DetailView, FormMixin, MultipleObjectMixin):
    model = Post
    template_name = 'post_detail.html'
    form_class = CommentForm
    queryset = Post.objects.filter(date_pub__year__gte=2020)
    paginate_by = 2
    success_url = '/'


    def get_context_data(self, **kwargs):
        object_list = Comment.objects.all()
        context = super().get_context_data(object_list=object_list,**kwargs)
        context['form'] = self.form_class
        context['comments'] = Comment.objects.all()
        return context


    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            self.object = self.get_object()
            object_list = Comment.objects.all()
            context = super().get_context_data(object_list=object_list, **kwargs)
            context['form'] = CommentForm
            return self.form_valid(form)
        else:
            self.object = self.get_object()
            object_list = Comment.objects.all()
            context = super().get_context_data(object_list=object_list, **kwargs)
            context['form'] = form
            return self.form_invalid(form)


    def form_valid(self, form):
        content = form.save(commit=False)
        content.user =  self.request.user
        content.content = form.cleaned_data['content']
        content.reply = form.cleaned_data['reply']
        comment_qs = None
        if content.reply:
            comment_qs = Comment.objects.get(id=content.reply.id)
        content.save()
        form.save()
        return redirect('/posts/')


    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))