"""
class PostList, где будет
отображаться список
объектов модели Post

class PostDetail, где будет
отображаться один объект Post,
и список комментариев с вложенностью
и пагинацией
"""
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView, MultipleObjectMixin
from django.views.generic.edit import FormView
from comments.models import Comment
from .forms import CommentForm
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
    queryset = Post.objects.filter(date_pub__year__gte=2020)
    paginate_by = 2
    success_url = '/'
    prefix = None
    initial = {}


    def get_context_data(self, **kwargs):
        object_list = Comment.objects.all()
        context = super().get_context_data(object_list=object_list,**kwargs)
        context['form'] = self.form_class
        context['comments'] = Comment.objects.all()
        return context


    def get_initial(self):
        return self.initial.copy()


    def get_prefix(self):
        return self.prefix


    def get_form_kwargs(self):
        '''
        Return the keyword arguments
        for instantiating
        the form
        '''
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
                'user': self.request.user
            })
        return kwargs


    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            self.object = self.get_object()
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
        return redirect(reverse('posts:post-list'))


    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
