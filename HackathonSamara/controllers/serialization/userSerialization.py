from rest_framework import serializers
from HackathonSamara.apps.main.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'login', 'password']
        read_only_fields = ['id']
