from django.contrib import admin
# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")   # Show these fields in the list view
    search_fields = ("title", "author__name")              # Add search bar
    list_filter = ("published_date",)  
admin.site.register(Book, BookAdmin)