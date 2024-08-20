from book import Book
from author import Author
from user import User


class Library:
    def __init__(self):
        self.books = {}
        self.authors = {}
        self.users = {}

    def _find_user_by_library_id(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                return user
        raise LookupError("Cannot find user with library_id: {}" % library_id)

    # User actions
    def add_user_to_library(self, user):
        self.users[user.get_library_id()] = user

    def add_borrowed_book(self, library_id, book):
        user = self.users[library_id]
        user.assign_borrowed_book(book)
        book.mark_as_borrowed(True)
        return f"\n* Book '{book}' checked out to {user.get_name()} *"
    
    def remove_returned_book(self, library_id, book):
        user = self.users[library_id]
        user.return_borrowed_book(book)
        book.mark_as_borrowed(False)
        return f"\n* Book '{book.get_title}' returned by {user.get_name()}. *"
    
    def find_user(self, library_id):
        if library_id not in self.users:
            return f"\n* User not found. *"
        else:
            user = self.users[library_id]
            return user.format()

    def display_all_users(self):
        for (library_id, user) in self.users.items():
            name = user.get_name()
            print(f"\nLibrary ID: {library_id}\n- Name: {name}")


    # Book actions
    def add_book_to_library(self, book):
        if book.title not in self.books:
            self.books[book.title] = {
                'Author': book.author,
                'Genre': book.genre,
                'Publication Date': book.publication_date,
                'Availability': book.availability
            }

    def get_availability(self, title):
        return self.books[title]["Availability"]
    
    def borrow_book(self, title):
        self.books[title]["Availability"] = "Borrowed"

    def return_book(self, title):
        self.books[title]["Availability"] = "Available"

    def find_book(self, title):
        if title not in self.books:
            return f"\n* Book not found. *"
        else:
            author = self.books[title]["Author"]
            genre = self.books[title]["Genre"]
            publication_date = self.books[title]["Publication Date"]
            availability = self.books[title]["Availability"]
            return f"\nTitle: {title}\n- Author: {author}\n- Genre: {genre}\n- Publication Date: {publication_date}\n- Availability: {availability}"
        
    def display_all_books(self):
        for title in self.books:
            author = self.books[title]["Author"]
            genre = self.books[title]["Genre"]
            publication_date = self.books[title]["Publication Date"]
            availability = self.books[title]["Availability"]
            print(f"\nTitle: {title}\n- Author: {author}\n- Genre: {genre}\n- Publication Date: {publication_date}\n- Availability: {availability}")


    # Author actions
    def add_author_to_library(self, author):
        self.authors[author.name] = {"Biography": author.biography}

    def find_author(self, author_name):
        if author_name not in self.authors:
            return f"\n* Author not found. *"
        else:
            biography = self.authors[author_name]["Biography"]
            return f"\nAuthor: {author_name}\n- Biography: {biography}"
        
    def display_all_authors(self):
        for author in self.authors:
            print(f"\n- Author: {author}")