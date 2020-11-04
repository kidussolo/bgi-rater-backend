from . import models, serializers
from rest_framework import generics

class Record_Audio(generics.ListCreateAPIView):
    """
    view which handle incoming request with audio file
    """
    queryset = models.RecordedAudio.objects.all()
    serializer_class = serializers.RecordedAudioSerializer


