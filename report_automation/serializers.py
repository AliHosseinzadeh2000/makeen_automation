from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Report, Course, Comment


class USerSerializer(serializers.ModelSerializer):
    student_reports = serializers.PrimaryKeyRelatedField(queryset=Report.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'student_reports']


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'number', 'date', 'student', 'description', 'study_duration']
        read_only_fields = ['student']
