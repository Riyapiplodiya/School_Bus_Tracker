from django.shortcuts import render, redirect
from accounts.models import UserModel
from students.models import Student
from bus.forms import BusForm,RouteForm,DriverForm,ConductorForm
from students.forms import StudentForm
from bus.models import Bus ,Route,Driver
from django.contrib.auth.decorators import login_required

@login_required
def school_dashboard(request):

    school = request.user.school

    total_buses = Bus.objects.filter(school=school).count()
    total_students = Student.objects.filter(school=school).count()
    total_drivers = Driver.objects.filter(school=school).count()
    total_conductors = UserModel.objects.filter(
        role="conductor",
        school=school
    ).count()

    buses = Bus.objects.filter(school=school)

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

@login_required
def create_bus(request):
    if request.user.role != "school":
        return redirect("login")
    school = request.user.school

    if request.method == "POST":
        form = BusForm(request.POST,school=request.user.school)

        if form.is_valid():

            bus_number = form.cleaned_data['bus_number']
            conductor = form.cleaned_data["conductor"]
            driver = form.cleaned_data["driver"]

            if Bus.objects.filter(bus_number=bus_number, school=school).exists():
                form.add_error("bus_number", "Bus already exists")

            elif Bus.objects.filter(conductor=conductor, school=school).exists():
                form.add_error("conductor", "Conductor already assigned")

            elif Bus.objects.filter(driver=driver, school=school).exists():
                form.add_error("driver", "Driver already assigned")

            else:
                bus = form.save(commit=False)
                bus.school = school   # 🔥 IMPORTANT
                bus.save()
                return redirect("school_dashboard")

    else:
        form = BusForm(school=request.user.school)

    return render(request, "school/create_bus.html", {"form": form})

def create_route(request):

    school = request.user.school

    if request.method == "POST":

        form = RouteForm(request.POST or None , school=request.user.school)

        if form.is_valid():

            route_name = form.cleaned_data['route_name']

            if Route.objects.filter(route_name=route_name, school=school).exists():
                form.add_error("route_name", "Route already exists")

            else:
                route = form.save(commit=False)
                route.school = school
                route.save()
                return redirect("school_dashboard")

    else:
        form = RouteForm(request.POST or None)

    return render(request, "school/create_route.html", {"form": form})

def add_student(request):

    school = request.user.school

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.school = school   # 🔥 IMPORTANT
            student.save()
            return redirect("school_dashboard")

    else:
        form = StudentForm(request.POST or None, school=request.user.school)

    return render(request, "school/add_student.html", {"form": form})

def create_driver(request):

    school = request.user.school

    if request.method == "POST":
        form = DriverForm(request.POST)

        if form.is_valid():
            driver = form.save(commit=False)
            driver.school = request.user.school   # 🔥 IMPORTANT
            driver.save()
            return redirect("school_dashboard")

    else:
        form = DriverForm(request.POST or None)

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

    school = request.user.school

    if request.method == "POST":

        form = ConductorForm(request.POST)

        if form.is_valid():

            conductor = form.save(commit=False)
            conductor.role = "conductor"
            conductor.school = school   # 🔥 IMPORTANT
            conductor.set_password(form.cleaned_data["password"])
            conductor.save()

            return redirect("school_dashboard")

    else:
        form = ConductorForm()

    return render(request, "school/add_conductor.html", {"form": form})