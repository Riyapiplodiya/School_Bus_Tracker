from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import UserModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password


def home(request):
    return render(request,"accounts/home.html")

@login_required
def user_list(request):
    users = UserModel.objects.all()
    return render(request, "accounts/user_list.html", {"users": users})


def signup_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        mobile = request.POST.get("mobile")
        role = request.POST.get("role")

        if UserModel.objects.filter(username=username ,role=role).exists():
            messages.error(request, "Username with same role already exists")
            return redirect("signup")

        try:
            validate_password(password)
            print(password)
            user = UserModel(
                username=username,
                email=email,
                mobile_number=mobile,
                role=role
            )
            user.set_password(password)
            user.full_clean()  
            user.save()
            messages.success(request, "Account created successfully")

            return redirect("login")

        except ValidationError as e:
            print(e)
            return render(request, "accounts/signup.html", {"errors": e.messages})

    return render(request, "accounts/signup.html")



def login_view(request):

    role = request.GET.get("role") or request.POST.get("role")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user_obj = UserModel.objects.get(username=username, role=role)
        except UserModel.DoesNotExist:
            return render(request, "accounts/login.html", {
                "error": "User not registered with this role",
                "role": role
            })

        # password check manually
        if not check_password(password, user_obj.password):
            return render(request, "accounts/login.html", {
                "error": "Invalid password",
                "role": role
            })

        # login user
        login(request, user_obj)

        if user_obj.role == "parent":
            return redirect("parent_dashboard")

        elif user_obj.role == "conductor":
            return redirect("conductor_dashboard")


        elif user_obj.role == "school":
            return redirect("school_dashboard")

    return render(request, "accounts/login.html", {"role": role})