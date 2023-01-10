from .views import PostList
from django.urls import path


urlpattern = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>', PostList.as_view(), name='post_detail'),
]
