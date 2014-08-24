from .models import Client, Gap, Notes, Day
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


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('date', 'dayofweek', 'unfilled')

# EOF
