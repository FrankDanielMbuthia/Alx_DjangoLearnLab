from django.contrib import admin
from .models import Book
class BookAdmin(admin.ModelAdmin):
    # Show these fields in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters on the right-hand sidebar
    list_filter = ("publication_year", "author")

    # Add search functionality (search bar at the top)
    search_fields = ("title", "author")
admin.site.register(Book, BookAdmin)
