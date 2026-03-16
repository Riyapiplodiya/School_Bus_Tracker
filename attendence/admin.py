from django.contrib import admin

# Register your models here.
from .models import Attendance

@admin.register(Attendance)
class MyModelAdmin(admin.ModelAdmin):

    fields = ['student','conductor','date','boarded_at','status',]