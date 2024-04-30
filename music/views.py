from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Album, Songs
from .serializers import ArtistSerializer, AlbumSerializer, SongsSerializer


class INDEXAPIView(APIView):
    def get(self, request):
        return Response({"get": "Hello world"})

    def post(self, request):
        return Response(data={"post": "This isn post request api"})


class ArtistAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data)


class AlbumAPIView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(data=serializer.data)


class SongsAPIView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(data=serializer.data)
