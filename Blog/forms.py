from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, user, Comment

#Form to fill Up when Signing Up Information
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length =100,required = True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

#Form to fill when Writing a Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("Title","Content")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("Content",)
