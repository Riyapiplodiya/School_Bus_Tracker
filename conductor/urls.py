from django.urls import path
from conductor.views import mark_attendence
from school.views import conductor_dashboard

urlpatterns = [

    path("dashboard/", conductor_dashboard, name="conductor_dashboard"),
    path("attendence/", mark_attendence, name="mark_attendence"),

]