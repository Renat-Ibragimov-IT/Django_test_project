from movies_app.models import Movie
from rest_framework import viewsets
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class Top10MoviesViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Movie.objects.order_by('-rating')[:10]
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)


class TopRandomMoviesViewSet(viewsets.ViewSet):

    def list(self, request, count):
        queryset = Movie.objects.order_by('-rating')[:int(count)]
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = MovieSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

