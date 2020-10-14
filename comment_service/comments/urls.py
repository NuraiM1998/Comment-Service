from django.urls import path, include
from .views import CommentCreate, CommentUpdate, CommentDelete, CommentReply

app_name='comments'
urlpatterns = [
    path('<int:post_id>/create/', CommentCreate.as_view(), name='create'),
    path('<int:comment_id>/reply/', CommentReply.as_view(), name='reply'),
    path('<int:pk>/update/', CommentUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', CommentDelete.as_view(), name='delete'),
]
