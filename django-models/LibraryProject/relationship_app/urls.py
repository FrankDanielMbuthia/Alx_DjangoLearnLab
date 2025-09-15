from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.index, name="index"),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

]