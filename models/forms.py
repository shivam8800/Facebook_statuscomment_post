from django import forms
from .models import Comment, Status

class PostComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comments_text',)