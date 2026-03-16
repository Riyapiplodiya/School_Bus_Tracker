from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import  Student
from accounts.models import UserModel


# Parent Form (for creating parent data)
# class ParentForm(forms.ModelForm):

#     class Meta:
#         model = Parent
#         fields = ['name', 'phone_number', 'email', 'address']


# Login Form
# class LoginForm(AuthenticationForm):

#     username = forms.CharField(
#         widget=forms.TextInput(attrs={
#             'class': 'input-field',
#             'placeholder': 'Enter Username'
#         })
#     )

#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'class': 'input-field',
#             'placeholder': 'Enter Password'
#         })
#     )

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields ="__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["parent"].queryset = UserModel.objects.filter(role="parent")