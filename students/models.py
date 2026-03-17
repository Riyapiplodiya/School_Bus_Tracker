from django.db import models
from accounts.models import UserModel
from bus.models import Bus,Route
from school.models import School

# class Parent(models.Model):
    

#     name = models.CharField(max_length=100)

#     phone_number = models.CharField(max_length=10)

#     email = models.EmailField()

#     address = models.TextField()

#     def __str__(self):
#         return self.name
    

class SchoolClass(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)

    class_name = models.CharField(max_length=20)

    section = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.class_name} - {self.section}"


class Student(models.Model):

    name = models.CharField(max_length=100)

    age = models.IntegerField()

    school_class = models.ForeignKey(
    SchoolClass,
    on_delete=models.CASCADE
    )

    parent = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        limit_choices_to={"role":"parent"},
        related_name="children"
    )

    bus = models.ForeignKey(
        Bus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    school=models.ForeignKey(School,on_delete=models.CASCADE)


    route = models.ForeignKey(
        Route,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    emergency_contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name