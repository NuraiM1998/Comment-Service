'''Форма комментариев'''
from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    '''Форма коментария'''
    content = forms.CharField(
                            label='',
                            widget=forms.Textarea(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Ответить',
                                    'rows': '4',
                                    'cols': '50'
                                    }
                                    )
                                    )
    class Meta:
        '''Объявление полей'''
        model = Comment
        fields = [
            'content', 'reply'
        ]
        widgets = {
        'content': forms.Textarea(attrs={'class': 'form-control',}),
       }
