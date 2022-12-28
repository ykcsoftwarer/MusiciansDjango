from rest_framework import serializers
from .models import Artist, lyric, Song, Album


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "first_name", "last_name", "artist_pic", "num_stars"]
        
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["artist", "artist", "cover", "released" ]
        
        
class lyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = lyric
        fields = ["title", "content" ]
        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["album", "artist", "name", "released", "lyric" ]
        

