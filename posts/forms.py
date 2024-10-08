from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'banner'] ### The fields of the Post model class in models.py