from django.urls import path
from students.views import parent_dashboard
from school.views import add_student

urlpatterns = [
    path("dashboard/", parent_dashboard, name="parent_dashboard"),
    path("add-student/", add_student, name="add_student"),
]