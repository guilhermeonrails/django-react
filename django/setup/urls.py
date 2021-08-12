from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from alurafy.views import BandaViewSet

router = routers.DefaultRouter()
router.register('Banda', BandaViewSet, basename='Bandas')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
