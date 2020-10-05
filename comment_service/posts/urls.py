from django.urls import path, include
from .views import *

app_name='posts'
urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<slug:slug>/', PostDetail.as_view(), name='post-detail'),
]