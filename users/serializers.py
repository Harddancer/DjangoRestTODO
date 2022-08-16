
from rest_framework import serializers
from .models import Users,Project,TODO

class UserSerializer(serializers.Serializer):
   address = serializers.CharField(max_length=30, blank=True)
   name_user = serializers.CharField(max_length=64)

class ProjectSerializer(serializers.Serializer):
    name_project = serializers.CharField(max_length=64)
    user = UserSerializer(many=True)

class TODOSerializer(serializers.Serializer):
    name_todo = serializers.CharField(max_length=64)
    text = serializers.CharField(max_length=64)
    date_creation = serializers.DateField
    date_update = serializers.DateField
    name_user = serializers.CharField(max_length=64)
    status = serializers.CharField(max_length=64)
    user = UserSerializer()

