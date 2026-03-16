from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from attendence.models import Attendance
from students.models import Student


@login_required
def parent_dashboard(request):
    # get students of logged in parent
    students = Student.objects.filter(parent=request.user)

    # latest attendance
    attendance = Attendance.objects.filter(
        student__in=students
    ).order_by("-boarded_at").first()

    context = {
        "attendance": attendance
    }

    return render(request, "students/parent_dashboard.html", context)
    