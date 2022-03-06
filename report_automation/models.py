from django.db import models
from django.contrib.auth.models import User


class Report(models.Model):
    number = models.PositiveSmallIntegerField()
    date = models.DateField()
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_reports')
    description = models.TextField(default='empty')
    study_duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return f'report num. {self.number} - {self.student}'



class Comment(models.Model):
    student = models.ForeignKey(User,  limit_choices_to={'groups__name': "students"}, on_delete=models.CASCADE, related_name='student_comments')
    teacher = models.ForeignKey(User,  limit_choices_to={'groups__name': "teachers"}, on_delete=models.CASCADE, related_name='teacher_comments')
    month_number = models.PositiveSmallIntegerField()
    text = models.TextField(default='empty')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.teacher.username} commented this for {self.student.username} in {self.created_at}'



class Course(models.Model):
    title = models.CharField(max_length=200)
    number = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True)
    students = models.ManyToManyField(User)
    teacher = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='teacher_courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.number}'
