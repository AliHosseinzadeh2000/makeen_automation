from django.contrib import admin
from .models import Report, Course, Comment


admin.site.register(Report)
admin.site.register(Course)
admin.site.register(Comment)