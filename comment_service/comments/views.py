'''CRUD of Comments'''
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from comments.forms import CommentForm
from .models import Comment, PostComment
from posts.models import Post


class CommentCreate(CreateView):
    '''Добавление комментариев'''
    form_class = CommentForm
    template_name = "comments/create_comment.html"
    success_url = reverse_lazy('posts:list')

    def form_valid(self, form):
        print(dir(form))
        comment = form.instance
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        comment.record = post
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CommentUpdate(UpdateView):
    '''Редактирование комментариев'''
    model = Comment
    form_class = CommentForm
    template_name = "comments/update_comments.html"
    success_url = reverse_lazy('posts:list')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CommentDelete(DeleteView):
    '''Удаление комментариев'''
    model = Comment
    template_name = "comments/delete_comment.html"
    success_url = reverse_lazy('posts:list')
