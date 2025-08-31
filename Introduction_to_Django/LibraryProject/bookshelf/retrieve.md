# Retrieve the book
book = Book.objects.get(title="1984")

# Display all attributes
book.__dict__

# Expected Output:
# {
#     'id': 1,
#     'title': '1984',
#     'author': 'George Orwell',
#     'publication_year': 1949,
#     '_state': <django.db.models.base.ModelState object at 0x...>
# }
