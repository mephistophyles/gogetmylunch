from django.shortcuts import render

from .models import Prop, Tag, Flair, GGMLUser
from .serializers import PropSerializer

from rest_framework import generics


class PropListCreate(generics.ListCreateAPIView):
    queryset = Prop.objects.all()
    serializer_class = PropSerializer