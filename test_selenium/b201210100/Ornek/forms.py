from django import forms
from .models import BlogPost,Industry,Comment,CommentIndustry

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'categories', 'date', 'description', 'read_more_link']

class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ['title', 'description', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class CommentIndustryForm(forms.ModelForm):
    class Meta:
        model = CommentIndustry
        fields = ['content']