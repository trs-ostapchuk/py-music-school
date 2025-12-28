from musician.models import Musician
from musician.serializer import MusicianSerializer
from rest_framework import viewsets


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
