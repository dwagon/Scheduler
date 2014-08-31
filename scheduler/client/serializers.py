from .models import Client, Notes
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'regularity', 'dayofweek', 'duration')


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('note', )


# EOF
