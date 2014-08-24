from rest_framework import generics
from .models import Client, Gap, Notes, Day
from .serializers import ClientSerializer, GapSerializer, NotesSerializer, DaySerializer


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class GapList(generics.ListCreateAPIView):
    queryset = Gap.objects.all()
    serializer_class = GapSerializer


class GapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gap.objects.all()
    serializer_class = GapSerializer


class NotesList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class DayList(generics.ListCreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class DayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

# EOF
