from rest_framework import routers
from .views import CourseViewSet, TestViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'tests', TestViewSet, basename='test')

urlpatterns = [
    path('', include(router.urls)),
]
