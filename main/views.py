from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Genre
from .serializers import *


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # def get_serializer_context(self):
    #     return {'request': self.request}


class MovieImageView(generics.ListAPIView):
    queryset = MovieImage.objects.all()
    serializer_class = MovieImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}