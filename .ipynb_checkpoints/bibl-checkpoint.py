from boobook import Book
books = [
    Book("Robinson Crusoe", "Daniel Defoe", 1719, 33),
    Book("Gulliver’s Travels", "Jonathan Swift", 1726, 39),
    Book("War and Peace", "Leo Tolstoy", 1869, 49),
    Book("The Brothers Karamazov", "Fyodor Dostoevsky", 1880,45)
]
for book in books:
    print(book.get_info())
most_expensive_book = Book.find_most_expensive(books)
if most_expensive_book:
    print("\nMost Expensive Book:")
    print(most_expensive_book.get_info())
books[1].set_stoplist(True)
print("\nAfter setting stoplist for 'Gulliver’s Travels':")
print(books[1].get_info())
books[0].censor("Daniel Defoe", True)
print("\nAfter censoring 'Robinson Crusoe' by 'Daniel Defoe':")
print(books[0].get_info())