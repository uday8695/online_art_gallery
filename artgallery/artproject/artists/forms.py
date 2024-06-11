from django import forms
from .models import Artists

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artists
        fields = '__all__'
