from .models import PostComment
from django import forms


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('name', 'email', 'body')