from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
)
from .import views
urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),  # here the class is PostListView and method is as_view()
    path('user/<str:username>/', UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), # here post/1 is the url of first post and as_view() is method of PostDetailView
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about,name='blog-about'),
]
