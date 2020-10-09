from django.urls import path, include
from .views import CommentCreate, CommentUpdate, CommentDelete

app_name='comments'
urlpatterns = [
    path('create/', CommentCreate.as_view(), name='create'),
    path('<int:pk>/update/', CommentUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', CommentDelete.as_view(), name='delete'),
]
