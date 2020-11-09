from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Comment, PostComment, CommentHierarchy
# from .models import Post, Comment
# admin.site.register(Post)
# @admin.register(Comment)
# class CommentAdmin(ImportExportModelAdmin):
#     pass

class CommentHierarchyAdmin(admin.ModelAdmin):
    list_display = ['parent', 'child', 'depth']

admin.site.register(Comment)
admin.site.register(PostComment)
admin.site.register(CommentHierarchy, CommentHierarchyAdmin)
