'''CRUD of Comments'''
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from comments.forms import CommentForm
from .models import Comment


class CommentCreate(CreateView):
    '''Добавление комментариев'''
    form_class = CommentForm
    template_name = "comments/create_comment.html"
    success_url = reverse_lazy('posts:list')


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
