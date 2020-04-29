from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from system.models import Customer

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This User doesnot Exist or Incorrect Password.")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")
        return super(UserLoginForm,self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
      ]

# class CustomerForm(forms.ModelForm):
#
#     class Meta:
#         model = Customer
#         fields = ('mobileno','birthdate', 'address','license_number','license_place')


# class SignUpForm(forms.ModelForm):
#
#     first_name = forms.CharField(max_length=256)
#     last_name = forms.CharField(max_length=256)
#     email = forms.EmailField()
#     mobileno = forms.IntegerField()
#     birthdate = forms.DateField()
#     address = forms.CharField(max_length=30)
#     license_number = forms.CharField(max_length=10)
#     license_place = forms.CharField(max_length=30)
#
#
#     class Meta:
#         model = Customer
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)

