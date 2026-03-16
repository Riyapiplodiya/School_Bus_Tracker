from django.db import models

# Create your models here.
from django.db import models
from students.models import Student
from accounts.models import UserModel


class Attendance(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    conductor = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)

    boarded_at = models.DateTimeField(auto_now_add=True)

    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ["student", "date"]
        
    def __str__(self):
        return f"{self.student.name} - {self.boarded_at}"