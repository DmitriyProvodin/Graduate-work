from rest_framework import serializers
from .models import Course, Section, Material, Test, Question, Choice, Attempt, Answer


class ChoiceSerializer(serializers.ModelSerializer):
class Meta:
model = Choice
fields = ('id','text') # не раскрываем is_correct


class QuestionSerializer(serializers.ModelSerializer):
choices = ChoiceSerializer(many=True, read_only=True)
class Meta:
model = Question
fields = ('id','text','order','choices')


class TestSerializer(serializers.ModelSerializer):
questions = QuestionSerializer(many=True, read_only=True)
class Meta:
model = Test
fields = ('id','title','time_limit_minutes','questions')


class MaterialSerializer(serializers.ModelSerializer):
tests = TestSerializer(many=True, read_only=True)
class Meta:
model = Material
fields = ('id','title','content','resource_file','tests')


class SectionSerializer(serializers.ModelSerializer):
materials = MaterialSerializer(many=True, read_only=True)
class Meta:
model = Section
fields = ('id','title','order','materials')


class CourseSerializer(serializers.ModelSerializer):
sections = SectionSerializer(many=True, read_only=True)
class Meta:
model = Course
fields = ('id','title','description','owner','sections')
read_only_fields = ('owner',)


def create(self, validated_data):
user = self.context['request'].user
return Course.objects.create(owner=user, **validated_data)