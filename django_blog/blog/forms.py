from django import forms
from .models import Post
from django.contrib.auth.models import User
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
    
# ProfileForm added
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] 

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="", 
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Write your comment..."})
    )

    class Meta:
        model = Comment
        fields = ["content"]