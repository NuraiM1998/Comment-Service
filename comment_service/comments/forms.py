'''Форма комментариев'''
from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    '''Форма коментария'''
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.user = self.user
        
        if commit:
            comment.save()
        
        return comment


    class Meta:
        '''Объявление полей'''
        model = Comment
        fields = [
            'content', 'reply'
        ]
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control',}),
        }
