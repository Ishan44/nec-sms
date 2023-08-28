import json

from django.db import models


class Student(models.Model):
    studentId = models.CharField(max_length=20, unique=True)
    studentEmail = models.EmailField()
    enrollmentDate = models.DateField()
    classYear = models.PositiveIntegerField()
    major = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    semester = models.CharField(max_length=20)
    creditsCompleted = models.PositiveIntegerField()
    creditsInProgress = models.PositiveIntegerField()
    totalCredits = models.PositiveIntegerField()
    graduationDate = models.DateField()
    transcript = models.TextField()
    contactEmail = models.EmailField()
    contactPhone = models.CharField(max_length=20)
    contactAddress = models.TextField()
    guardianRelationship = models.CharField(max_length=50)
    guardianName = models.CharField(max_length=100)
    guardianAddress = models.TextField()
    guardianContactNo = models.CharField(max_length=20)
    address = models.TextField()
    isHosteller = models.BooleanField(default=False)
    hostelDetails = models.TextField()

    class Meta:
        db_table = 'student'

    def __str__(self):
        return json.dump(self.__dict__, indent=4)
