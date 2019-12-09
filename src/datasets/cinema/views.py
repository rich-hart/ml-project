from rest_framework import viewsets
from .models import TVShow, Movie
from .serializers import MovieSerializer, TVShowSerializer
from django.db.models.query import QuerySet
class MovieViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
#    queryset = Movie.nodes.all()
#    queryset = QuerySet(Movie).all()

    serializer_class = MovieSerializer
    # FIXME: try to use QuerySet class instead
    def get_queryset(self):
        return Movie.nodes.all()

    def perform_create(self, serializer):
        import ipdb;ipdb.set_trace()
        serializer.save()
class TVShowViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
#    queryset = TVShow.nodes.all()
#    queryset = QuerySet(TVShow).all()
    serializer_class = TVShowSerializer
    # FIXME: try to use QuerySet class instead
    def get_queryset(self):
        return TVShow.nodes.all()

