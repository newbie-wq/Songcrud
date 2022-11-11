from .models import Song
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['artiste_id', 'title']