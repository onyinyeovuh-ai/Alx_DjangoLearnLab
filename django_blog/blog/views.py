from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


# ---------------------------
# LIST VIEW
# ---------------------------
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


# ---------------------------
# DETAIL VIEW
# ---------------------------
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


# ---------------------------
# CREATE VIEW
# ---------------------------
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# ---------------------------
# UPDATE VIEW
# ---------------------------
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# ---------------------------
# DELETE VIEW
# ---------------------------
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Comment
from .forms import CommentForm

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs["post_id"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.object.post.id})
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Comment
        form_class = CommentForm
        template_name = "blog/comment_form.html"

        def test_func(self):
           comment = self.get_object()
           return self.request.user == comment.author

        def get_success_url(self):
            return reverse_lazy("post-detail", kwargs={"pk": self.object.post.id})
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Comment
        template_name = "blog/comment_confirm_delete.html"

        def test_func(self):
            comment = self.get_object()
            return self.request.user == comment.author

        def get_success_url(self):
            return reverse_lazy("post-detail", kwargs={"pk": self.object.post.id})
    
