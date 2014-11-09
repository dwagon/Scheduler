from .models import Gap
from rest_framework import serializers


class GapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gap
        fields = ('desc', 'start', 'end', 'recurring')

# EOF
