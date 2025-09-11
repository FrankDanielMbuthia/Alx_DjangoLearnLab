author = Author.objects.get(name="J.K. Rowling")  
books = author.book_set.all()   # default reverse lookup

library = Library.objects.get(name="Central Library")
books = library.books.all()   # because it's a ManyToMany

librarian = Librarian.objects.get(library=library)
librarian = library.librarian   # Django auto creates this attribute
