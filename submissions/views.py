from thanimaBackend.helpers import GenericResponse
from rest_framework import generics
from .serializers import *
from .models import Event
from .models import Participant

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
class CreateSubmissionView(generics.CreateAPIView):
    def post(self, request,*args, **kwargs):
        participant = Participant.objects.get(user_id = request.user.id)
        event = Event.objects.get(id=request.data['event_id'])
        file = request.data['file']
        submission = Submission(event = event, file = file,participant = participant)
        submission.save()
        return GenericResponse("success",submission)
