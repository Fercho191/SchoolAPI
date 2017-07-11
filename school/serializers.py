from rest_framework import serializers
from .models import School, Student, Activity, Assignment


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedRelatedField(
        many=True, view_name='student-detail', queryset=Student.objects)

    class Meta:
        model = School
        fields = ('id', 'name', 'created', 'students')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    school = serializers.ReadOnlyField(source='school.name')
    schoolId = serializers.ReadOnlyField(source='school.id')

    class Meta:
        model = Student
        fields = ('id', 'name', 'school', 'schoolId')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    school = serializers.ReadOnlyField(source='school.name')
    schoolId = serializers.ReadOnlyField(source='school.id')

    class Meta:
        model = Activity
        fields = ('id', 'name', 'school', 'schoolId', 'created')


class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    studentId = serializers.ReadOnlyField(source='student.id')
    activity = serializers.ReadOnlyField(source='activity.name')
    activityId = serializers.ReadOnlyField(source='activity.id')

    class Meta:
        model = Assignment
        fields = ('id', 'activity', 'activityId', 'student', 'studentId')
