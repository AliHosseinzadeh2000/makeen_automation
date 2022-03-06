from rest_framework import serializers
from .models import Report, Course, Comment


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'number', 'date', 'student', 'description', 'study_duration']
        read_only_fields = ['student']
