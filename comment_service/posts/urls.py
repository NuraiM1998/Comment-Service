''' Пути к постам и коментам '''
from django.urls import path
from .views import PostList, PostDetail, PostCommentChildren

app_name='posts'
urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('<slug:slug>/', PostDetail.as_view(), name='detail'),
    path('<int:parentcomment_id>/subcomments/', PostCommentChildren.as_view(), name='subcomments'),
]
