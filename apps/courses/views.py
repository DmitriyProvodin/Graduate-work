from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Section, Material, Test, Question, Choice, Attempt, Answer
from .serializers import CourseSerializer, TestSerializer, SubmitAttemptSerializer
from apps.accounts.permissions import IsTeacherOrAdmin, IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils import timezone

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ('create','update','partial_update','destroy'):
            return [IsTeacherOrAdmin()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get_permissions(self):
        if self.action in ('create','update','partial_update','destroy'):
            return [IsOwnerOrAdmin()]
        return [IsAuthenticated()]

    @action(detail=True, methods=['post'], url_path='submit')
    def submit(self, request, pk=None):
        test = self.get_object()
        serializer = SubmitAttemptSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answers = serializer.validated_data['answers']
        attempt = Attempt.objects.create(user=request.user, test=test)
        correct = 0
        total = test.questions.count()
        for ans in answers:
            qid = ans['question_id']
            choice_id = ans.get('choice_id')
            try:
                question = test.questions.get(id=qid)
            except Question.DoesNotExist:
                continue
            choice = None
            if choice_id:
                try:
                    choice = question.choices.get(id=choice_id)
                except Choice.DoesNotExist:
                    choice = None
            Answer.objects.create(attempt=attempt, question=question, choice=choice)
            if choice and choice.is_correct:
                correct += 1
        score = (correct / total * 100) if total > 0 else 0.0
        attempt.score = score
        attempt.finished_at = timezone.now()
        attempt.save()
        return Response({'attempt_id': attempt.id, 'score': score})
