from django import forms
from .models import Artista, Album, Cancion

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'artistas']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'artistas': forms.SelectMultiple(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'size': '5'})  # size is optional for scrollable
        }

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['titulo', 'album', 'artistas']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'album': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'artistas': forms.SelectMultiple(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'size': '5'})  # size is optional for scrollable
        }