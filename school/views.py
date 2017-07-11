# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.decorators import list_route
from school.models import School, Student, Activity, Assignment
from school.serializers import (
    SchoolSerializer,
    StudentSerializer,
    ActivitySerializer,
    AssignmentSerializer
)

class SchoolViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    # @list_route()
    # def students(self, request, pk):
    #     students = Student
    #     return Response(snippet.highlighted)


class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
