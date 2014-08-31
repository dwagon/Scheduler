from rest_framework import generics
from .models import Gap
from .serializers import GapSerializer


class GapList(generics.ListCreateAPIView):
    queryset = Gap.objects.all()
    serializer_class = GapSerializer


class GapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gap.objects.all()
    serializer_class = GapSerializer

# EOF
