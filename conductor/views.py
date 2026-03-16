from django.shortcuts import render
from students.models import Student


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

            if status == "present":

                attendance = Attendance.objects.create(
                    student=student,
                    conductor=request.user,
                    status=True
                )

                # get time
                time = datetime.now().strftime("%I:%M %p")

                # parent email
                parent_email = student.parent.email

                # send email
                send_mail(
                    "Bus Boarding Alert",
                    f"Hello {student.parent.name},\n\nYour child {student.name} has boarded the bus at {time}.",
                    settings.EMAIL_HOST_USER,
                    [parent_email],
                    fail_silently=True
                )

    return render(
        request,
        "conductor/attendence.html",
        {"students": students}
    )