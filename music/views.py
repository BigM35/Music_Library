from music.models import Music
from music.serializers import MusicSerializer   
from rest_framework import generics

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer