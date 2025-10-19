from django import forms
from django.contrib.auth.models import User
from .models import Member

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["age", "address", "phone", "membership_plan"]
