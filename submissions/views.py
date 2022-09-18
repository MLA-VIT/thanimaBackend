from thanimaBackend.helpers import GenericResponse
from rest_framework import generics
from .serializers import *
from .models import Event

class AllEventsView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get(self, request, *args, **kwargs):
        response = super().list(self, request, *args, **kwargs)
        return GenericResponse("success",response.data)

class CreateEventView(generics.CreateAPIView):
    serializer_class = EventSerializer

    def post(self, request, *args, **kwargs):
        response = super().create(self, request, *args, **kwargs)
        return GenericResponse("success",response.data)