from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("books/", views.list_books, name="book_list"),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path("register/", views.register, name="register"),
    path("login/", views.RoleBasedLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("librarian_dashboard/", views.librarian_dashboard, name="librarian_dashboard"),
    path("member_dashboard/", views.member_dashboard, name="member_dashboard"),
    path("books/add_book/", views.add_book, name="add_book"),
    path("books/edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("books/delete_book/<int:book_id>/", views.delete_book, name="delete_book"),

]

