from django.urls import path
from .views import INDEXAPIView, ArtistAPIView, AlbumAPIView, SongsAPIView

urlpatterns = [
    path('landing/', INDEXAPIView.as_view(), name='index'),
    path('artists/', ArtistAPIView.as_view(), name='artists'),
    path('albums/', AlbumAPIView.as_view(), name='albums'),
    path('songs/', SongsAPIView.as_view(), name='songs'),
]

