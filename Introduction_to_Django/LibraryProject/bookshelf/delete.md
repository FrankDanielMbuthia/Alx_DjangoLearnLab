# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Expected Output:
# (1, {'app_name.Book': 1})   # 1 row deleted

# Confirm deletion by retrieving all books
Book.objects.all()

# Expected Output:
# <QuerySet []>
