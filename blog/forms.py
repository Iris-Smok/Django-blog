"""
Comment form class
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    class CommentForm
    """
    class Meta:
        """
        class Meta
        """
        model = Comment
        fields = ('body',)
