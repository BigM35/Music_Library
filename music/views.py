from music.models import Song
from music.serializers import MusicSerializer   
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
# TODO USe the @api view first
@api_view(['GET','POST'])
def music_list(request):
    if request.method == 'GET':
        music = Song.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data = request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk = pk)
    if request.method == 'GET':
        serializer = MusicSerializer(song);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicSerializer(song, data = request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
# TODO: Refactor after MVP to use Snippets (started) below
# class MusicList(generics.ListCreateAPIView):
#    queryset = Music.objects.all()
#    serializer_class = MusicSerializer


# class SongDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Music.objects.all()
#    serializer_class = MusicSerializer