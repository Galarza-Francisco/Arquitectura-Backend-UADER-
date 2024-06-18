from django.urls import path
from musica_api import views

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('artistas/', views.artistas_rest, name='artistas-rest'),
    path('index_artistas/', views.index_artistas, name='index_artistas'),
    path('nuevo_artista/', views.NuevoArtista.as_view(), name='nuevo_artista'),
    path('albumes/', views.albumes_rest, name='albumes-rest'),
    path('index_albumes/', views.index_albumes, name='index_albumes'),
    path('nuevo_album/', views.NuevoAlbum.as_view(), name='nuevo_album'),
    path('canciones/', views.canciones_rest, name='canciones-rest'),
    path('index_canciones/', views.index_canciones, name='index_canciones'),
    path('nueva_cancion/', views.NuevaCancion.as_view(), name='nueva_cancion'),
]
