from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register_view,
    profile_view,
    logout_view,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    # Auth views
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("logout/", logout_view, name="logout"),

    # Blog views
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),    
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"), 
]

from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns += [
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-add"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]

from .views import search_view, posts_by_tag_view

urlpatterns += [
    path("search/", search_view, name="search"),
    path("tags/<str:tag_name>/", posts_by_tag_view, name="posts-by-tag"),
]