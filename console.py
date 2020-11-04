import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("John", "Tolkien")
author_repository.save(author1)

book1 = Book("Lord of the Rings", "Fantasy", "Allen and Unwin", author1)
book_repository.save(book1)

author2 = Author("Joanna", "Rowling")
author_repository.save(author2)

book2 = Book("Harry Potter", "Children\'s", "Penguin", author2)
book_repository.save(book2)

pdb.set_trace()

