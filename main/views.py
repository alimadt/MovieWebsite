from django.db.models import Q
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

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        serializer = MovieSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def get_serializer_context(self):
    #     return {'request': self.request}


class MovieImageView(generics.ListAPIView):
    queryset = MovieImage.objects.all()
    serializer_class = MovieImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}
