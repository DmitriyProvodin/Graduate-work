from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Test, Attempt, Question, Choice, Answer
from .serializers import CourseSerializer, TestSerializer, SubmitAttemptSerializer
from apps.accounts.permissions import IsTeacherOrAdmin, IsOwnerOrAdmin


class CourseViewSet(viewsets.ModelViewSet):
queryset = Course.objects.all()
serializer_class = CourseSerializer


def get_permissions(self):
if self.action in ('create','update','partial_update','destroy'):
return [IsTeacherOrAdmin()]
return [permissions.IsAuthenticated()]


def perform_create(self, serializer):
serializer.save(owner=self.request.user)


class TestViewSet(viewsets.ModelViewSet):
queryset = Test.objects.all()
serializer_class = TestSerializer


def get_permissions(self):
if self.action in ('create','update','partial_update','destroy'):
return [IsOwnerOrAdmin()]
return [permissions.IsAuthenticated()]


@action(detail=True, methods=['post'], url_path='submit')
def submit(self, request, pk=None):
serializer = SubmitAttemptSerializer(data=request.data)
serializer.is_valid(raise_exception=True)
# обработка: создать Attempt, ответы, вернуть результат
# ... (логика подсчёта очков) ...
return Response({'score': 100})