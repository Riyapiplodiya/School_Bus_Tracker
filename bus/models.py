from django.db import models
from accounts.models import UserModel
from school.models import School

class Driver(models.Model):

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    license_number = models.CharField(max_length=50,unique=True)
    
    school=models.ForeignKey(School,on_delete=models.CASCADE)


    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Bus(models.Model):

    bus_number = models.CharField(max_length=20,unique=True)

    driver = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True
    )

    conductor = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={"role": "conductor"}
    )
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    capacity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bus_number


class Route(models.Model):

    route_name = models.CharField(max_length=100)

    start_location = models.CharField(max_length=200)

    end_location = models.CharField(max_length=200)

    bus = models.ForeignKey(
        Bus,
        on_delete=models.CASCADE,
        related_name="routes"
    )
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return self.route_name
    
