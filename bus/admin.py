from django.contrib import admin

# Register your models here.
from .models import Driver,Bus,Route

@admin.register(Driver)
class MyModelAdmin(admin.ModelAdmin):

    fields = ['name','phone','license_number','address','created_at',]
    
@admin.register(Bus)
class MyModelAdmin(admin.ModelAdmin):

    fields = ['bus_number','driver','conductor','capacity','created_at',]
    

@admin.register(Route)
class MyModelAdmin(admin.ModelAdmin):

    fields = ['route_name','start_location','end_location','bus',]
    
