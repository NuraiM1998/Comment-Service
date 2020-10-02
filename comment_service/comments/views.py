import csv
from .forms import CommentForm
from .models import Post, Comment
from django.views.generic import View, ListView
from djqscsv import render_to_csv_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_detail(request, slug=None): # Comment form with replies
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter_by_instance(post)
    initial_data = {
        "content_type": post.get_content_type,
        "object_id": post.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        print(c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first() 
        content_type = ContentType.objects.get(model=c_type)
        new_comment, created = Comment.objects.get_or_create(
                            user=request.user,
                            content_type=content_type,
                            object_id=obj_id,
                            content=content_data,
                            parent=parent_obj
                        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    comments=post.comments
    return render(request, 'comments/post_detail.html', context={
        'post': post,
        'comments': comments,
        'comment_form': form
    })

def posts_list(request): # Listing all Post objects
    posts = Post.objects.all()
    return render(request, 'comments/index.html', {'posts': posts})



def export(request): # Export Comment objects into csv file 
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['user', 'parent_id', 'content', 'timestamp'])

    comments = Comment.objects.all().values_list('user', 'parent_id', 'content', 'timestamp')
    for comment in comments:
        writer.writerow(comment)
    response['Content-Disposition'] = 'attachment; filename="comments.csv"'
    return response