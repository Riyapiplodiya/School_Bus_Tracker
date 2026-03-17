from django.shortcuts import render
from students.models import Student
from datetime import date
from attendence.models import Attendance
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

def mark_attendence(request):

    students = Student.objects.filter(
        bus__conductor=request.user
    )

    if request.method == "POST":

        for student in students:

            status = request.POST.get(str(student.id))

            attendance, created = Attendance.objects.get_or_create(
                student=student,
                date=date.today(),
                defaults={
                    "conductor": request.user,
                    "status": status == "present"
                }
            )

            # ✅ Update if already exists
            if not created:
                attendance.status = (status == "present")
                attendance.save()

            # ✅ Send email ONLY first time when marked present
            if created and status == "present":

                time = datetime.now().strftime("%I:%M %p")

                parent_email = student.parent.email

                send_mail(
                    "Bus Boarding Alert",
                    f"Hello {student.parent.username},\n\n"
                    f"Your child {student.name} has boarded the bus at {time}.",
                    settings.EMAIL_HOST_USER,
                    [parent_email],
                    fail_silently=True
                )

    return render(
        request,
        "conductor/attendence.html",
        {"students": students}
    )