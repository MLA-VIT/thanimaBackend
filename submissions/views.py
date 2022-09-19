import re
from thanimaBackend.helpers import GenericResponse
from rest_framework import generics
from .serializers import *
from .models import Event
from .models import Participant
from datetime import datetime
from rest_framework.permissions import *
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages
import pyrebase
import os


firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
storage = firebase.storage()

class AllEventsView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()

    def get(self, request, *args, **kwargs):
        response = super().list(self, request, *args, **kwargs)
        return GenericResponse("success",response.data)

class CreateEventView(generics.CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        response = super().create(self, request, *args, **kwargs)
        return GenericResponse("success",response.data)

class CreateSubmissionView(generics.CreateAPIView):

    def submit_file(self, file, filename, accepted_formats):
        ext = file.name.split('.')[-1]
        filename = f"{filename}.{ext}"
        if ext in accepted_formats:
            file_save = default_storage.save(filename, file)
            url = storage.child("files/" + filename).put("submissions/" + filename).get_url()
            print(url)
            delete = default_storage.delete(filename)
            return url

    def post(self, request,*args, **kwargs):
        participant = Participant.objects.get(user_id = request.user.id)
        event = Event.objects.get(id=request.data['event_id'])
        if event.deadline: # Check Deadline
            if datetime.now() > event.deadline:
                raise Exception(422, "deadline passed for submission.")
        if event.file_submission: # File Submission
            file = request.FILES.get('file', None)
            if file is None:
                print(request.FILES)
                raise Exception(422, "file submission expected, but not received.")
            print(file)
            url = self.submit_file(file, request.user.reg_no, event.accepted_formats)
        else: # Link Submission
            url_rx = r"^(http(s)?:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
            url = request.data.get('file', None)
            if url is None:
                raise Exception(422, 'link submission expected, but not received.')
            if re.search(url_rx, url) is None:
                raise Exception(422, 'invalid URL passed.')
        try: # User can make as many submissions as they want till deadline
            submission = Submission.objects.get(participant = participant,event = event)
            submission.file = url
        except Submission.DoesNotExist:
            submission = Submission(event = event, file = url,participant = participant)
        submission.save()
        return GenericResponse("success",submission)
