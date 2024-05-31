
from django import forms
from .models import Artworks

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artworks
        fields = ['Artwork_id','title','artist_id','artist_name','medium','dimensions','category','price','description','status','image_url']
        widgets = {
            'Artwork_id':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter artist id'}),
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter artwork title'}),
            'artist_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter artist id'}),
            'artist_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter artist name'}),
            'medium': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter art medium'}),
            'dimensions': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter artwork dimensions'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter artwork category'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter artwork price'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter sales status'}),
            'image_url':forms.URLInput(attrs={'class': 'form-control', 'placeholder':'enter image url'}),
        }
