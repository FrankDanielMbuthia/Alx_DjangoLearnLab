from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, MemberProfileForm
from .models import Member, User, MembershipPlan, Payment
from rest_framework import viewsets
from .serializers import UserSerializer, MembershipPlanSerializer, PaymentSerializer

def register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        profile_form = MemberProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            member = profile_form.save(commit=False)
            member.user = user
            member.save()
            return redirect("login")
    else:
        user_form = UserRegisterForm()
        profile_form = MemberProfileForm()
    return render(request, "members/register.html", {"user_form": user_form, "profile_form": profile_form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
    return render(request, "members/login.html")


@login_required
def dashboard(request):
    member = Member.objects.get(user=request.user)
    return render(request, "members/dashboard.html", {"member": member})


def logout_view(request):
    logout(request)
    return redirect("login")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MembershipPlanViewSet(viewsets.ModelViewSet):
    queryset = MembershipPlan.objects.all()
    serializer_class = MembershipPlanSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer