from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Report, Course, Comment
from .serializers import USerSerializer, ReportSerializer, GradeListSerializer, GradeDetailSerializer
from .permissions import ReportPermission, GradePermission, UserPermission
from . import tools


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = USerSerializer
    permission_classes = (UserPermission,)



class ReportViewSet(viewsets.ModelViewSet, ReportPermission):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (ReportPermission,)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)



class GradeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Report.objects.all()
    serializer_action_classes = {
        'list': GradeListSerializer,
        'retrieve': GradeDetailSerializer
    }
    permission_classes = (GradePermission,)


    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.action == 'retrieve':
            instance = self.get_object()

            context['most_study_duration'] = tools.get_most_study_duration(instance.student)
            context['least_study_duration'] = tools.get_least_study_duration(instance.student)
            context['last_30_days_reports'] = tools.get_last_30_days_reports(instance.student)
            context['last_30_days_total'] = tools.get_last_30_days_total(instance.student)

        return context


    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class
