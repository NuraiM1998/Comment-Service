from django.urls import path, include
from .views import CommentCreate, CommentUpdate, CommentDelete

app_name='comments'
urlpatterns = [
    path('create/', CommentCreate.as_view(), name='create'),
    path('<int:pk>/update/', CommentUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', CommentDelete.as_view(), name='delete'),
    # path('posts/<str:slug>/', post_detail, name='post_detail'),
    # path('export_comments/', export, name='export_comments'),
    # path('export_comments_excel/', export_comments_xls, name='export_comments_excel')
]
