from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.models import Post
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #makes it so that modifications are applied to the model class
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image']