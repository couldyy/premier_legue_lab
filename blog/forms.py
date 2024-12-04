from django import forms
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class ChangeAccountDateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CreateUser(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    username = forms.CharField(label='Username', widget=forms.TextInput())
    name = forms.CharField(label='Name', widget=forms.TextInput(), required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput())
    agree_statement = forms.BooleanField(label='', help_text='Some text you need to agree with', widget=forms.CheckboxInput())

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'name',  'password1', 'password2', 'agree_statement')

class LoginUser(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise ValidationError('Invalid login')

    class Meta:
        model = User
        fields = ('username', 'password')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text']
        widgets = {
            'comment_content': forms.Textarea(),
        }



