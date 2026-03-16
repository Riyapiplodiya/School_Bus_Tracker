from django.urls import path
from school import views

urlpatterns = [
    path("dashboard/",views.school_dashboard,name="school_dashboard"),
    path("create-bus/", views.create_bus, name="create_bus"),
    path("create-route/", views.create_route, name="create_route"),
    path("create-driver/", views.create_driver, name="create_driver"),
    # path("add-parent/", views.add_parent, name="add_parent"),
    path("add-conductor/", views.add_conductor, name="add_conductor"),
]