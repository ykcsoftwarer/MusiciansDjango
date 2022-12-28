from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ArtistSerializer, AlbumSerializer, lyricSerializer, SongSerializer


from .models import Artist, Album, lyric, Song



# Create your views here.

@api_view()
def home(request):
    return Response({'home': 'This is the musicans page...'})

# def home_page(response):
    
#artist

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def artist_create(request):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
             "message": f'Artist Created Succesfully'
        }
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
           
                 
@api_view(['PUT'])
def artist_update(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    serializer = ArtistSerializer(instance=artist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
             "message": f'Artist updated Succesfully'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
                         
@api_view(['DELETE'])
def artist_Delete(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    artist.delete()
    message = {
             "message": f'Artist deleted Succesfully'
        }
    return Response(message)
    
#!Album

@api_view(['GET'])
def albums_list(request):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def album_create(request):
   serializer = AlbumSerializer(data = request.data)
   if serializer.is_valid():
    serializer.save()
    message = {
        "message:" f'Album Created Successfully'
    }
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def album_update(request, pk):
    album = get_object_or_404(Album, id=pk)
    serializer = AlbumSerializer(instance=album, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Album updated succesfully....'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def album_delete(request, pk):
    album = get_object_or_404(Album, id=pk)
    album.delete()
    message = {
        "message": 'Album deleted succesfully....'
    }
    return Response(message)


# Lyric

@api_view(['GET'])
def lyrics_list(request):
    lyrics = lyric.objects.all()
    serializer = lyricSerializer(lyrics, many=True)
  
    return Response(serializer.data)


@api_view(['POST'])
def lyric_create(request):
   serializer = lyricSerializer(data = request.data)
   if serializer.is_valid():
    serializer.save()
    message = {
        "message:" f'Lyrics Created Successfully'
    }
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def lyric_update(request, pk):
    lyric = get_object_or_404(lyric, id=pk)
    serializer = lyricSerializer(instance=lyric, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Lyric updated succesfully....'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def lyric_delete(request, pk):
    lyric = get_object_or_404(lyric, id=pk)
    lyric.delete()
    message = {
        "message": 'Album deleted succesfully....'
    }
    return Response(message)
# Song

@api_view(['GET'])
def songs_list(request):
    songs = Song.objects.all()
   
    serializer = SongSerializer(songs, many=True)
    
    return Response(serializer.data)

@api_view(["POST"])
def song_create(request):
   serializer = SongSerializer(data=request.data)
   if serializer.is_valid():
    serializer.save()
    message = {
        "message:" f'Song Created Successfully'
    }
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def song_update(request, pk):
    song = get_object_or_404(song, id=pk)
    serializer = SongSerializer(instance=Song, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Song updated succesfully....'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def song_delete(request, pk):
    song = get_object_or_404(Song, id=pk)
    song.delete()
    message = {
        "message": 'Song deleted succesfully....'
    }
    return Response(message)