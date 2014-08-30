from .models import Client, Gap, Notes
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'regularity', 'dayofweek', 'duration')


class GapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gap
        fields = ('start', 'end')


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('note', )


# EOF
