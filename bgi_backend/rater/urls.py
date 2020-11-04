from django.urls import path
from . import views

urlpatterns = [
    path('audio', views.Record_Audio.as_view())
]