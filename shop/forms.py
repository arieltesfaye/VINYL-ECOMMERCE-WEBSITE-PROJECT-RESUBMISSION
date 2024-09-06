from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'price', 'cover_image', 'keywords']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)