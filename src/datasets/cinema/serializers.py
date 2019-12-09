from rest_framework import serializers

from .models import Movie, TVShow

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'released']

class TVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ['id', 'title', 'released']
