from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Report, Course, Comment
from .serializers import ReportSerializer, USerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = USerSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
