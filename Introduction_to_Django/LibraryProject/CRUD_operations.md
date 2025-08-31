# CRUD Operations for Book Model

## Create

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
# Expected Output:
# <Book: 1984 by George Orwell (1949)>

book = Book.objects.get(title="1984")
book.__dict__
# Expected Output:
# {
#     'id': 1,
#     'title': '1984',
#     'author': 'George Orwell',
#     'publication_year': 1949,
#     '_state': <django.db.models.base.ModelState object at 0x...>
# }

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected Output:
# (1, {'app_name.Book': 1})

Book.objects.all()
# Expected Output:
# <QuerySet []>
