from rest_framework import generics
from .models import Client, Notes
from .serializers import ClientSerializer, NotesSerializer


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class NotesList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


# EOF
