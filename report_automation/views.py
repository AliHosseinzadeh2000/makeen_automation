from rest_framework import viewsets, permissions
from .models import Report, Course, Comment
from .serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
