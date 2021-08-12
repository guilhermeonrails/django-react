from rest_framework import serializers
from alurafy.models import Banda

class BandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banda
        fields = '__all__'
