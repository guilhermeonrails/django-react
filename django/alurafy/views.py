from rest_framework import viewsets
from alurafy.models import Banda
from alurafy.serializers import BandaSerializer

class BandaViewSet(viewsets.ModelViewSet):
    queryset = Banda.objects.all()
    serializer_class = BandaSerializer