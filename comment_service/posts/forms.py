from comments.models import Comment
from django import forms
from .models import Post
from django.forms import ModelForm, HiddenInput



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]
        widgets = {
        'content': forms.Textarea(attrs={'class': 'form-control',}),
       }