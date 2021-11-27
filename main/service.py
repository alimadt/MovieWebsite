from django_filters import rest_framework as filters

from main.models import Movie


class MovieFilter(filters.FilterSet):
    year = filters.RangeFilter()

    class Meta:
        model = Movie
        fields = ['year']
