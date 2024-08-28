from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'e.g. test','class':'form-control'}),
            'content': forms.Textarea(attrs={'placeholder':'e.g. anything','class':'form-control'}),
            'image': forms.FileInput(attrs={'placeholder':'e.g. any img','class':'form-control'}),
            'published_at': forms.DateTimeInput(attrs={'class':'form-control'}),
            'created_at': forms.TextInput(attrs={'placeholder':'e.g. shirt','class':'form-control'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'placeholder':'e.g. shirt','class':'form-control'}),
            'status': forms.Select(attrs={'placeholder':'e.g. shirt','class':'form-control'})
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image','tags','status']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'e.g. test','class':'form-control'}),
            'content': forms.Textarea(attrs={'placeholder':'e.g. anything','class':'form-control'}),
            'image': forms.FileInput(attrs={'placeholder':'e.g. any img','class':'form-control'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'placeholder':'e.g. shirt','class':'form-control'}),
            'status': forms.Select(attrs={'placeholder':'e.g. shirt','class':'form-control'})
        }
