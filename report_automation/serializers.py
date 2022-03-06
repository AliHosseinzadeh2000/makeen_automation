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



class GradeListSerializer(serializers.Serializer):
    student = serializers.CharField(read_only=True)

    class Meta:
        model = Report
        fields = ['student']



class GradeDetailSerializer(serializers.Serializer):
    student = serializers.CharField(read_only=True)
    most_study_duration = serializers.SerializerMethodField()
    least_study_duration = serializers.SerializerMethodField()


    def get_most_study_duration(self, Report):
        return self.context['most_study_duration']

    def get_least_study_duration(self, Report):
        return self.context['least_study_duration']

        
    class Meta:
        model = Report
        fields = ['student', 'most_study_duration', 'least_study_duration']
