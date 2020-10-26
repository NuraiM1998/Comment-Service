'''Форма комментариев'''
from django import forms
from comments.models import Comment, PostComment, Node


class PostCommentForm(forms.ModelForm):
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

    # id = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        '''Объявление полей'''
        model = PostComment
        fields = [
            'content',
        ]
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control',}),
        }
        

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

    # id = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        '''Объявление полей'''
        model = Comment
        fields = [
            'content',
        ]
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control',}),
        }


class NodeForm(forms.ModelForm):
    '''Форма коментария'''
    
    # def __init__(self, user, *args, **kwargs):
    #     self.user = user
    #     super().__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     comment = super().save(commit=False)
    #     comment.user = self.user
        
    #     if commit:
    #         comment.save()
        
    #     return comment

    # id = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        '''Объявление полей'''
        model = Node
        fields = [
            'name', 'parent', 'post', 'user'
        ]
        widgets = {
            'parent': forms.HiddenInput(),
            'post': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }
        