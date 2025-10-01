from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin


class BookAdmin(admin.ModelAdmin):
    # Show these fields in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters on the right-hand sidebar
    list_filter = ("publication_year", "author")

    # Add search functionality (search bar at the top)
    search_fields = ("title", "author")
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)