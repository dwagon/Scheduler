from .models import Visit
from rest_framework import serializers


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('client', 'good', 'date', 'note')


# EOF
