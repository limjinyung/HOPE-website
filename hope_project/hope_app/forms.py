from .models import PostComment, User
from django import forms


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='username',
                    widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control',
                                                  'required': True, 'type': 'text', 'style': 'height:50px;'}))
    password = forms.CharField(label='password',
                    widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control',
                                                  'required': True, 'type': 'password', 'style': 'height:50px;'}))

    class Meta:
        model = User
        fields = ['username','password',]


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('name', 'email', 'body')