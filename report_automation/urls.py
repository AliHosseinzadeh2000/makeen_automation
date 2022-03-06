from django.urls import path, include
from rest_framework.routers import DefaultRouter
from report_automation import views

router = DefaultRouter()
router.register(r'reports', views.ReportViewSet, basename='reports')
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
