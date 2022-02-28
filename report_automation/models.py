from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
    number = models.PositiveSmallIntegerField()
    date = models.DateField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default='empty')
    study_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'report num. {self.number} - {self.student}'
