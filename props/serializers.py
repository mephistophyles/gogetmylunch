from rest_framework import serializers
from .models import Prop, GGMLUser, Tag, Flair
from django.contrib.auth.models import User

class PropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prop
        fields = '__all__'
