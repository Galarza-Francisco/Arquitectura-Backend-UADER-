from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Artista, Album, Cancion
from .forms import ArtistaForm, AlbumForm, CancionForm
from .serializers import ArtistaSerializer, AlbumSerializer, CancionSerializer


def get_all_artistas():
    artistas = Artista.objects.all().order_by('nombre')
    serializer = ArtistaSerializer(artistas, many=True)
    return serializer.data

def get_all_albumes():
    albumes = Album.objects.all().order_by('titulo')
    serializer = AlbumSerializer(albumes, many=True)
    return serializer.data

def get_all_canciones():
    canciones = Cancion.objects.all().order_by('titulo')
    serializer = CancionSerializer(canciones, many=True)
    return serializer.data


def artistas_rest(request):
    artistas = get_all_artistas()
    return JsonResponse(artistas, safe=False)

def albumes_rest(request):
    albumes = get_all_albumes()
    return JsonResponse(albumes, safe=False)

def canciones_rest(request):
    canciones = get_all_canciones()
    return JsonResponse(canciones, safe=False)


def index_artistas(request):
    artistas = get_all_artistas()
    return render(request, 'index_artistas.html', {'Artistas': artistas})

def index_albumes(request):
    albumes = get_all_albumes()
    return render(request, 'index_albumes.html', {'Albumes': albumes})

def index_canciones(request):
    canciones = get_all_canciones()
    return render(request, 'index_canciones.html', {'Canciones': canciones})


def Home(request):
    artistas = Artista.objects.all()
    albumes = Album.objects.all()
    canciones = Cancion.objects.all()
    return render(request, 'home.html', {
        'Artistas': artistas,
        'Albumes': albumes,
        'Canciones': canciones,
    })


class NuevoArtista(CreateView):
    model = Artista
    form_class = ArtistaForm
    template_name = 'form_artistas.html'
    success_url = reverse_lazy('home')

class NuevoAlbum(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'form_album.html'
    success_url = reverse_lazy('home')

class NuevaCancion(CreateView):
    model = Cancion
    form_class = CancionForm
    template_name = 'form_cancion.html'
    success_url = reverse_lazy('home')
