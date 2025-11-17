from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),              # Blog homepage showing all posts
    path('post/<int:pk>/', views.post_detail, name='post-detail'),  # Post detail with comments
    path('post/<int:pk>/like/', views.like_post, name='like-post'), # Like/unlike a post
]
