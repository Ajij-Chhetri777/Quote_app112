from django import forms 
from app.models import Quote, Comment, Reply
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class PostForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["line","categories"]

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['dialogue','quotes','user']
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['comment','replied']

