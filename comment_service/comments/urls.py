from django.urls import path, include
from .views import (
    CommentCreate, 
    CommentUpdate, 
    CommentDelete,
    PostCommentReply,
    PostCommentView
    )

app_name='comments'
urlpatterns = [
    path('<int:post_id>/create/', CommentCreate.as_view(), name='create'),
    path('create_comment/', PostCommentView.as_view(), name='create_com'),
    # path('<int:comment_id>/reply/', CommentReply.as_view(), name='reply'),
    path('<int:postcomment_id>/reply_post_comment/', PostCommentReply.as_view(), name='postcomment_reply'),
    path('<int:pk>/update/', CommentUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', CommentDelete.as_view(), name='delete'),
]
