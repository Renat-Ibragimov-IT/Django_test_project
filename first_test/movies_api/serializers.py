from movies_app.models import Movie, Actor
from rest_framework import serializers


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['name']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    actors = ActorSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ['name', 'description', 'release_date', 'rating', 'duration',
                  'vote', 'actors']

