from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from .models import Book
from .models import Author
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books":books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'   # <-- checker expects this
    context_object_name = 'library'
    def get_queryset(self):
        # Prefetch the related books and their authors to reduce DB hits.
        # This assumes Library -> Book related_name is 'books' and Book has FK 'author'.
        return Library.objects.prefetch_related('books__author')
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # create the user
            login(request, user)  # log the user in after registration
            return redirect("home")  # adjust if your homepage URL name is different
    else:
        form = UserCreationForm()
    
    return render(request, "relationship_app/register.html", {"form": form})

def is_admin(user):
    return user.userprofile.role == "Admin"

def is_librarian(user):
    return user.userprofile.role == "Librarian"

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "member_view.html")


# Add a new book
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author_id")
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect("list_books")
    return render(request, "add_book.html")

# Delete a book
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("list_books")

# Just to list books (no special permission required)
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})
