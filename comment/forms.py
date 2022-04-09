from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    # rating = forms.IntegerField()
    class Meta:
        model = Comment
        fields = ['text', 'rating']
