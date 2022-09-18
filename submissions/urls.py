from django.urls import path, include
from .views import *

urlpatterns = [
    path('',AllEventsView.as_view()),
    path('add/',CreateEventView.as_view())
]