
# drivers/forms.py
from django import forms
from .models import Artists

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artists
        fields = ['Artist_id','artist_name','artist_age','category','experience','earnings','no_of_drawings_made','created_at']
       