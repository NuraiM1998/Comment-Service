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
from django.core.paginator import Paginator
from django.views import View
from django.core import serializers
from django.shortcuts import get_object_or_404
from comments.models import Comment, PostComment, CommentHierarchy
from comments.forms import PostCommentForm
from .models import Post


class PostList(ListView):
    """Список объектов модели Post"""
    model = Post
    template_name = 'post_list.html'


    def get_queryset(self):
        return Post.objects.order_by('date_pub').reverse()


class PostDetail(DetailView):
    """
    один объект Post,
    и список комментариев с вложенностью
    и пагинацией
    """
    model = Post
    template_name = 'post_detail.html'
    # form_class = PostCommentForm
    success_url = reverse_lazy('posts:list')
    paginate_by = 3


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_visits = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_visits + 1
        context['comments'] = PostComment.objects.all()
        context['top_comments'] = PostComment.objects.filter(parent__isnull=True)
        context['sub_child'] = self.object.comments.filter(parent__isnull=False)
        context['post_comment_form'] = PostCommentForm(user=self.request.user, initial={'user': self.request.user, 'record': self.object})
        context['num_visits'] = num_visits
        depth = [dep for dep in PostComment.objects.filter(parent__isnull=True)]
        # print(self.object.comments.depth())
        print('dir', dir(PostComment.objects.filter(parent__isnull=True).filter(parents__depth__gte=0)))
        
        # print('dir', dir(self.object.comments.filter(parent__isnull=True)))
        # print(self.object.comments.filter(parent__isnull=True))

        return context


    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class PostCommentChildren(View):

    model = Post
    template_name = 'post_detail.html'


    def get(self, request, *args, **kwargs):
        id_ = self.kwargs.get('parentcomment_id')
        post_comment = get_object_or_404(PostComment, pk=id_)
        hie = get_object_or_404(CommentHierarchy, pk=id_)
        # print(hie.parent.content)
        # print('POST COMMENT', post_comment)
        # print('POST COMMENT >>>>', post_comment.children.all())
        # print('POST COMMENT DIR', dir(post_comment.content))
        children = PostComment.objects.filter(parents__parent=id_)
        child = [child for child in post_comment.children.all()]
        # print('depth', post_comment.depth.depth)


        # print('Children', dir(child))
        # print()
        # print('Children', child)
        data = {
            'has_children': children.exists(),
            'children': list(children.values())
        }
        return JsonResponse(data)
