from django.shortcuts import render, redirect
from accounts.models import UserModel
from students.models import Student
from bus.forms import BusForm,RouteForm,DriverForm,ConductorForm
from students.forms import StudentForm
from bus.models import Bus ,Route,Driver

def school_dashboard(request):
    total_buses = Bus.objects.count()
    total_students = Student.objects.count()
    total_drivers = Driver.objects.count()
    total_conductors = UserModel.objects.filter(role="conductor").count()

    buses = Bus.objects.all()

    context = {
        "total_buses": total_buses,
        "total_students": total_students,
        "total_drivers": total_drivers,
        "total_conductors": total_conductors,
        "buses": buses
    }

    return render(request,"school/school_dashboard.html",context)

def conductor_dashboard(request):
    return render(request,"conductor/conductor_dashboard.html")

def create_bus(request):

    if request.method == "POST":
        form = BusForm(request.POST)

        if form.is_valid():

            bus_number = form.cleaned_data['bus_number']
            conductor = form.cleaned_data["conductor"]
            driver = form.cleaned_data["driver"]

            if Bus.objects.filter(bus_number=bus_number).exists():
                form.add_error("bus_number", "Bus already exists")

            elif Bus.objects.filter(conductor=conductor).exists():
                form.add_error("conductor", "Conductor already assigned")

            elif Bus.objects.filter(driver=driver).exists():
                form.add_error("driver", "Driver already assigned")

            else:
                form.save()
                return redirect("school_dashboard")

    else:
        form = BusForm()

    return render(request, "school/create_bus.html", {"form": form})

def create_route(request):

    if request.method == "POST":

        form = RouteForm(request.POST)

        if form.is_valid():

            route_name = form.cleaned_data['route_name']

            if Route.objects.filter(route_name=route_name).exists():
                form.add_error("route_name", "Route already exists")

            else:
                form.save()
                return redirect("school_dashboard")

    else:
        form = RouteForm()

    return render(request, "school/create_route.html", {"form": form})

def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("school_dashboard")

    else:
        form = StudentForm()

    return render(request, "school/add_student.html", {"form": form})

def create_driver(request):

    if request.method == "POST":
        form = DriverForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("school_dashboard")

    else:
        form = DriverForm()

    return render(request, "school/create_driver.html", {"form": form})

# def add_parent(request):

#     if request.method == "POST":

#         form = ParentForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect("school_dashboard")

#     else:
#         form = ParentForm()

#     return render(request, "school/add_parent.html", {"form": form})

def add_conductor(request):

    if request.method == "POST":

        form = ConductorForm(request.POST)

        if form.is_valid():

            conductor = form.save(commit=False)
            conductor.role = "conductor"
            conductor.set_password(form.cleaned_data["password"])
            conductor.save()

            return redirect("school_dashboard")

    else:
        form = ConductorForm()

    return render(request, "school/add_conductor.html", {"form": form})