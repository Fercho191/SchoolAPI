# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class School(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "%s" % (self.name)


class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "%s" % (self.name)


class Activity(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "%s" % (self.name)


class Assignment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student)
    activity = models.ForeignKey(Activity)

    class Meta:
        ordering = ('created',)
