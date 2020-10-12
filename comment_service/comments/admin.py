from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Comment, PostComment
# from .models import Post, Comment
# admin.site.register(Post)
# @admin.register(Comment)
# class CommentAdmin(ImportExportModelAdmin):
#     pass

admin.site.register(Comment)
admin.site.register(PostComment)
