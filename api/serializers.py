from rest_framework import serializers
from .models import Class, Assignment

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model= Class
        fields=('className',)

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Assignment
        fields=('className',"name","grade")