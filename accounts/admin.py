from django.contrib import admin

# Register your models here.
from .models import UserModel

@admin.register(UserModel)
class MyModelAdmin(admin.ModelAdmin):

    fields = ['username','password','mobile_number','role','email',]
    
   