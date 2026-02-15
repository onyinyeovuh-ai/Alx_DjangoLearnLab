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

from . import views

urlpatterns += [
    path("post/<int:post_id>/comments/new/", views.add_comment, name="comment-add"),
    path("comments/<int:comment_id>/edit/", views.edit_comment, name="comment-edit"),
    path("comments/<int:comment_id>/delete/", views.delete_comment, name="comment-delete"),
]