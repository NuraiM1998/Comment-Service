from comments.models import Comment
from django import forms
from django.forms import ModelForm, HiddenInput
from django.views.generic.edit import CreateView


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['timestamp']
        widgets = {'content' : HiddenInput()}
# class CommentForm(forms.Form):
#     content_type = forms.CharField(widget=forms.HiddenInput)
#     object_id = forms.IntegerField(widget=forms.HiddenInput)
#     content = forms.CharField(label = '', widget=forms.Textarea)
    # class Meta:
    #     model = Comment
    #     fields = ('content_type', 'object_id', 'content')
    #     widgets = {
    #         'content_type': forms.HiddenInput,
    #         'object_id': forms.HiddenInput,
    #     }