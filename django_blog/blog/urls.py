from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    register_view,
    profile_view,
    logout_view,
)

urlpatterns = [
    # Auth views
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("logout/", logout_view, name="logout"),

    # Blog views
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),      # NEW
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # UPDATE
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),  # DELETE
]

from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns += [
    path("post/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="comment-add"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-edit"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]