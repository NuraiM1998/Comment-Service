from django.urls import path, include
from .views import *

app_name='comments'
urlpatterns = [
    path('posts/', posts_list, name='post_list'),
    path('posts/<str:slug>/', post_detail, name='post_detail')
]