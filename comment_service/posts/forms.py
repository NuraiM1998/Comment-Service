from comments.models import Comment
from django import forms
from django.forms import ModelForm, HiddenInput



class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ответить', 'rows': '4', 'cols': '50'}))
    class Meta:
        model = Comment
        fields = [
            'content', 'reply'
        ]
        widgets = {
        'content': forms.Textarea(attrs={'class': 'form-control',}),
       }