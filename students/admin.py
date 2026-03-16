from django.contrib import admin

# Register your models here.
from .models import SchoolClass,Student


   
@admin.register(SchoolClass)
class MyModelAdmin(admin.ModelAdmin):

    fields = ['class_name','section',]

@admin.register(Student)
class MyModelAdmin(admin.ModelAdmin):

    fields = ['name','age','school_class','parent','bus','route','emergency_contact',]

