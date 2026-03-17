from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from school.models import School
ROLE_CHOICES = [
        ('parent', 'Parent'),
        ('conductor', 'Conductor'),
        ('school', 'School')
    ]

phone_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="Mobile number must be exactly 10 digits"
    )

class UserModel(AbstractUser):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(
        max_length=10,
        validators=[phone_validator],
        blank=True,
        null=True
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True,blank=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["username", "role"],
                name="unique_username_role"
            )
        ]

    def clean(self):
        if self.role in ['parent','conductor'] and not self.mobile_number:
            raise ValidationError("Mobile number required for parent and conductor.")

    def __str__(self):
        return f"{self.username} - {self.role}"