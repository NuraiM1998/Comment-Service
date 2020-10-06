from .models import Post
from .forms import CommentForm
from comments.models import Comment
from comments.forms import CommentCreateForm
from datetime import datetime
from django.http import Http404
from django.utils import timezone
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, FormView, FormMixin
from polymorphic.formsets import polymorphic_modelformset_factory, PolymorphicFormSetChild


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'


    def get_queryset(self):
        return Post.objects.order_by('date_pub').reverse()


class PostDetail(DetailView, FormMixin):
    model = Post
    template_name = 'post_detail.html'
    form_class = CommentForm
    queryset = Post.objects.filter(date_pub__year__gte=2020)
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['comments'] = Comment.objects.all()
        return context


    def post(self, request, *args, **kwargs):
        # self.object = self.get_object()
        # form = self.get_form()
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = CommentForm
            return self.form_valid(form)
        else:
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = form
            return self.form_invalid()


    def form_valid(self, form):
        content = form.save(commit=False)
        content.user =  self.request.user
        content.content = form.cleaned_data['content']
        content.save()
        form.save()
        return redirect('/posts/')


    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


    # def post(self, request, *args, **kwargs):
    #     data = {
    #          'form-TOTAL_FORMS': '1',
    #          'form-INITIAL_FORMS': '0',
    #          'form-MAX_NUM_FORMS': '',
    #          'form-0-title': '',
    #          'form-0-pub_date': '',
    #     }
    #     # form = self.form_class(request.POST)
    #     formset = CommentFormset(data)
    #     if request.method == "POST":
    #         formset = CommentFormset(request.POST or None, request.FILES or None, queryset=Comment.objects.all())
    #         instances = formset.save(commit=False)
    #         for instance in instances:
    #             instance.content = self.cleaned_data['content']
    #             if instance.is_valid():
    #                 instance.save()
    #     else:
    #         formset = CommentFormset(queryset=Comment.objects.all())

    #     return render(request, self.template_name, {'form': formset})


# class CommentView(View):
#     form_class = CommentFormset
#     # initial = {'key': 'value'}
#     template_name = 'post_detail.html'


#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})


#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if request.method == "POST":
#             formset = form(request.POST, request.FILES, queryset=Comment.objects.all())
#             if formset.is_valid():
#                 formset.save()
#         else:
#             formset = form(queryset=Comment.objects.all())

#         return render(request, self.template_name, {'form': form})