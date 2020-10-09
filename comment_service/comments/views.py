import csv
import xlwt
# from .forms import CommentForm
import datetime
from .models import Comment
from comments.forms import CommentForm
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from djqscsv import render_to_csv_response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



class CommentCreate(CreateView):
    form_class = CommentForm
    template_name = "comments/create_comment.html"
    success_url = reverse_lazy('posts:list')


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/update_comments.html"
    success_url = reverse_lazy('posts:list')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CommentDelete(DeleteView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/delete_comment.html"
    success_url = reverse_lazy('posts:list')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    
    
# пока что эти комментарии снизу не уберу


# def export(request): # Export Comment objects into csv file 
#     response = HttpResponse(content_type='text/csv')
#     writer = csv.writer(response)
#     writer.writerow(['user', 'parent_id', 'content', 'timestamp'])

#     comments = Comment.objects.all().values_list('user', 'parent_id', 'content', 'timestamp')
#     for comment in comments:
#         writer.writerow(comment)
#     response['Content-Disposition'] = 'attachment; filename="comments.csv"'
#     return response


# def export_comments_xls(request):
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="comments.xls"'

#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('Comments Data') # this will make a sheet named Comments Data

#     # Sheet header, first row
#     row_num = 0

#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True

#     columns = ['user', 'parent_id', 'content', 'timestamp']

#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

#     # Sheet body, remaining rows
#     font_style = xlwt.XFStyle()

#     rows = Comment.objects.all().values_list('user', 'parent_id', 'content', 'timestamp')
#     rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
#     for row in rows:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)

#     wb.save(response)

#     return response