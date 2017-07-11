from rest_framework import serializers
from .models import School, Student, Activity, Assignment


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedRelatedField(
        many=True, view_name='student-detail', queryset=Student.objects)

    class Meta:
        model = School
        fields = ('id', 'name', 'created', 'students')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    school = serializers.HyperlinkedRelatedField(
        view_name='student-detail', queryset=School.objects)

    class Meta:
        model = Student
        fields = ('id', 'name', 'school')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    school = serializers.HyperlinkedRelatedField(
        view_name='student-detail', queryset=School.objects)

    class Meta:
        model = Activity
        fields = ('id', 'name', 'school', 'created')


class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    activity = serializers.HyperlinkedRelatedField(
        view_name='student-detail', queryset=Activity.objects)
    student = serializers.HyperlinkedRelatedField(
        view_name='student-detail', queryset=Student.objects)

    class Meta:
        model = Assignment
        fields = ('id', 'activity', 'student')
