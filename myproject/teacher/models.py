from django.db import models
from django.contrib.auth.models import User

class StudentRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()

    subject = models.CharField(max_length=100)
    marks = models.FloatField()

    attendance = models.FloatField()
    semester = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"