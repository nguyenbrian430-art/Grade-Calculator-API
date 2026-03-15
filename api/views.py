from rest_framework import viewsets
from .models import Class,Assignment
from .serializers import ClassSerializer, AssignmentSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset=Class.objects.all()
    serializer_class=ClassSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset=Assignment.objects.all()
    serializer_class=AssignmentSerializer