from django.urls import path
from .views import user_list,login_view,signup_view,home

urlpatterns = [
    path('', home, name='home'),
    path('users/', user_list, name='user_list'),
    path('login/', login_view, name='login'),
    path('signup/',signup_view,name='signup'),
     
]