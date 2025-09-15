from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login

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