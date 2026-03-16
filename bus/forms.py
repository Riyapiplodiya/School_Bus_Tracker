from django import forms
from .models import Bus,Route,Driver
from accounts.models import UserModel


class BusForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = ["bus_number", "driver", "conductor", "capacity"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # conductors already assigned to buses
        assigned_conductors = Bus.objects.values_list("conductor", flat=True)

        # show only conductors with role='conductor' and not assigned
        self.fields["conductor"].queryset = UserModel.objects.filter(
            role="conductor"
        ).exclude(id__in=assigned_conductors)
        



class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = ["route_name", "start_location", "end_location", "bus"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        assigned_buses = Route.objects.values_list("bus", flat=True)

        self.fields["bus"].queryset = Bus.objects.exclude(
            id__in=assigned_buses
        )
    
class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ["name", "phone", "license_number", "address"]
        
        
class ConductorForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["username", "email", "mobile_number","password"]