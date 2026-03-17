from django import forms
from .models import Bus,Route,Driver
from accounts.models import UserModel


class BusForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = ["bus_number", "driver", "conductor", "capacity"]

    def __init__(self, *args, **kwargs):
        school = kwargs.pop("school", None)   # 🔥 get school
        super().__init__(*args, **kwargs)

        if school:
            # conductors already assigned in THIS school only
            assigned_conductors = Bus.objects.filter(
                school=school
            ).values_list("conductor", flat=True)
            # show only available conductors of THIS school
            self.fields["conductor"].queryset = UserModel.objects.filter(
                role="conductor",
                school=school
            ).exclude(id__in=assigned_conductors)

            # also filter drivers (VERY IMPORTANT)
            assigned_drivers = Bus.objects.filter(
                school=school
            ).values_list("driver", flat=True)

            self.fields["driver"].queryset = Driver.objects.filter(
                school=school
            ).exclude(id__in=assigned_drivers)

class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = ["route_name", "start_location", "end_location", "bus"]
        
    def __init__(self, *args, **kwargs):
        school=kwargs.pop("school",None)
        super().__init__(*args, **kwargs)

        if school:
            assigned_buses = Route.objects.filter(
                school=school
            ).values_list("bus", flat=True)

            self.fields["bus"].queryset = Bus.objects.filter(
                school=school
            ).exclude(id__in=assigned_buses)
    
class DriverForm(forms.ModelForm):
    print("driver form==============")
    class Meta:
        model = Driver
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        print("DriverForm INIT CALLED") 
        school = kwargs.pop("school", None)   # 🔥 VERY IMPORTANT
        super().__init__(*args, **kwargs)

        if school:
                # Example: if driver has relation fields, filter them
            pass
        
class ConductorForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["username", "email", "mobile_number","password"]