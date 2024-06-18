from rest_framework import serializers
from .models import Artista, Album, Cancion

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artistas = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = '__all__'

class CancionSerializer(serializers.ModelSerializer):
    artistas = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cancion
        fields = '__all__'
