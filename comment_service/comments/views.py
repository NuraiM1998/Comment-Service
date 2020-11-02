'''CRUD of Comments'''
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from comments.forms import  PostCommentForm
from .models import Comment, PostComment
from posts.models import Post


class CommentCreate(CreateView):
    '''Добавление комментариев'''
    form_class = PostCommentForm
    template_name = "comments/create_comment.html"
    success_url = reverse_lazy('posts:list')

    def form_valid(self, form):
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
    form_class = PostCommentForm
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


# class CommentReply(CreateView):
#     '''Добавление ответов на комментарии'''
#     form_class = CommentForm
#     template_name = "comments/reply_comment.html"
#     success_url = reverse_lazy('posts:list')


#     def form_valid(self, form):
#         comment = form.instance
#         parent_comment = get_object_or_404(Comment, pk=self.kwargs.get('comment_id'))
#         comment.reply = parent_comment  
#         return super().form_valid(form)


#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.request.user
#         return kwargs


class PostCommentReply(CreateView):
    '''Добавление ответов на комментарии'''
    form_class = PostCommentForm
    template_name = "comments/reply_comment.html"
    success_url = reverse_lazy('posts:list')


    def form_valid(self, form):
        comment = form.instance
        print(dir(comment))
        print(comment)
        parent_comment = get_object_or_404(PostComment, pk=self.kwargs.get('postcomment_id'))
        comment.parent = parent_comment  
        return super().form_valid(form)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PostCommentView(CreateView):
    form_class = PostCommentForm
    template_name = "comments/reply_comment.html"
    success_url = reverse_lazy('posts:list')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs['request'] = self.request
        kwargs['user'] = self.request.user
        return kwargs
