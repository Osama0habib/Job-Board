from rest_framework import serializers
from .models import Job


class JobSerializable(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'