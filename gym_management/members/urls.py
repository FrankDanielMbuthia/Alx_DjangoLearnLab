from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MembershipPlanViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"plans", MembershipPlanViewSet)
router.register(r"payments", PaymentViewSet)


urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
    path("api/", include(router.urls)),
]
