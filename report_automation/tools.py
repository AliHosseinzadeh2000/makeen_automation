from datetime import datetime, timedelta
from .models import Report, Course, Comment


def get_most_study_duration(user):
    last_30_days = datetime.now() - timedelta(days=30)
    most_study_duration = Report.objects.filter(created_at__gte=last_30_days).filter(student__exact=user).latest('study_duration')
    return most_study_duration.study_duration


def get_least_study_duration(user):
    last_30_days = datetime.now() - timedelta(days=30)
    least_study_duration = Report.objects.filter(created_at__gte=last_30_days).filter(student__exact=user).earliest('study_duration')
    return least_study_duration.study_duration


def get_last_30_days_total(user):
    sum = 0
    for report in get_last_30_days_reports(user):
        sum += report.study_duration.total_seconds()
    return timedelta(seconds=sum)


def get_last_30_days_reports(user):
    last_30_days = datetime.now() - timedelta(days=30)
    last_30_days_reports = Report.objects.filter(created_at__gte=last_30_days).filter(student__exact=user)
    return last_30_days_reports
