# Library Management System Project

Library Management System is a command-line-based application to streamline the management of users, books, and resources within a library. This program was built using Python Programming Language while applying Object-Oriented Programming (OOP) principles and implementing an enhanced User Interface. It is a robust system that allows users to browse, borrow, return, and explore a collection of books. 
 
## Requirements:
* This project requires the following modules:
    - Python [Python Downloads](https://www.python.org/downloads/)
    - datetime (`import datetime`)
    - REGEX (`import re`)

## Installation:
*** **GitHub Repository** ***

[Module4-MiniProject Repository](https://github.com/Tmiseray/Module4-MiniProject)

*** **Cloning Option** ***
* If you have Git Bash installed, you can clone the repository using the URL
1. Create a 'Clone' Folder
2. Within the folder, right-click for Git Bash
3. From the GitHub Repository, click on the '<> Code' button and copy the link provided
4. Paste the link into your Git Bash and click 'Enter'
* If you have GitHub Desktop, when you click on the '<> Code' button you will have an option to 'Open with GitHub Desktop'
* If you have Visual Studio Code, when you click on the '<> Code' button you will have an option to 'Open with Visual Studio'
* [HTTPS] (https://github.com/Tmiseray/Module4-MiniProject-Library.git)
* [SSH] (git@github.com:Tmiseray/Module4-MiniProject-Library.git)
* [GitHubCLI] (`gh repo clone Tmiseray/Module4-MiniProject-Library`)

*** **Download Option** ***
1. From the GitHub Repository, click on the '<> Code' button
2. Click on 'Download Zip'
3. Extract contents of Zip file

## Features:

### User Interface (UI):
* [Main Module for Running Program](user_interface.py)
* Includes imports from other custom modules for all classes needed for functionality
* Once program begins running, instantiates `UserInterface` class, provides a welcome message to the user, and then calls the Main Menu `ui.main_menu()`.
    - When the class is instantiated `__init__(self)`, it establishes other class instances for use in menus
* There are 4 menus with additional features in the `UserInterface` class:
    - **Main Menu**
    - **User Operations**
    - **Book Operations**
    - **Author Operations**
* Each menu includes:
    - User-friendly format with specific options to choose from
    - While loops to ensure the menu is always provided to the user until no longer needed
    - `try` & `except` blocks for specific error handling of user inputs
#### *Main Menu:*
* `main_menu(self)`
* Provides 4 options to choose from:

1. User Operations:
    - Sends the user to the User Operations Menu `user_operations()`
2. Book Operations:
    - Sends the user to the Book Operations Menu `book_operations()`
3. Author Operations:
    - Sends the user to the Author Operations Menu `author_operations()`
4. Quit:
    - Provides the user a grateful message for using the system
        > .\~* Thank you for using Library Management System! *\~.

        > \* Exiting program... \*
    - Breaks from the loop
    - `finally`: terminates the program
#### *User Operations:*
* `user_operations(self)`
* Provides 4 options to choose from:
1. Add a New User
    - Sends the user to the `UserInput` class for use of `add_user()` method
2. View User Details
    - Sends the user to the `UserInput` class for use of `view_user_details()` method
3. Display All Users
    - Provides the user a title for the Users List
    > \*\* List of All Users: \*\*
    - Calls to the `Library` class for use of `display_all_users()` method
4. Return to Main Menu
    - Advises the user of the action:
    > \* Returning to Main Menu... \*
    - Sends the user back to the `main_menu(self)` method
#### *Book Operations:*
* `book_operations(self)`
* Provides 6 options to choose from:
1. Add a New Book
    - Sends the user to the `UserInput` class for use of `add_book()` method
2. Borrow a Book
    - Sends the user to the `UserInput` class for use of `borrow_book()` method
3. Return a Book
    - Sends the user to the `UserInput` class for use of `return_book()` method
4. Search for a Book
    - Sends the user to the `UserInput` class for use of `search_for_book()` method
5. Display All Books
    - Provides the user a title for the library collection
    > \*\* Full Library Collection: \*\*
    - Calls to the `Library` class for use of `display_all_books()` method
6. Return to Main Menu
    - Advises the user of the action:
    > \* Returning to Main Menu... \*
    - Sends the user back to the `main_menu(self)` method
#### *Author Operations:*
* `author_operations(self)`
* Provides 4 options to choose from:
1. Add a New Author
    - Sends the user to the `UserInput` class for use of `add_author()` method
2. View Author Details
    - Sends the user to the `UserInput` class for use of `view_author_details()` method
3. Display All Authors
    - Provides the user a title for the Authors List
    > \*\* All Authors in Library: \*\*
    - Calls to the `Library` class for use of `display_all_authors()` method
4. Return to Main Menu
    - Advises the user of the action:
    > \* Returning to Main Menu... \*
    - Sends the user back to the `main_menu(self)` method

### User Inputs & Validations:
* [Module for User Inputs & Validations](user_input.py)
* This module handles all user inputs
* Includes imports from built-in and other custom modules for all classes needed for functionality
* There are 2 classes with their own methods in this module:
    - **ValidateInputs**
    - **UserInput**
#### *Validation & Formatting:*
* `class ValidateInputs`
* Once instantiated, `__init__(self)` establishes instances for REGEX patterns and datetime module for use
* There are 3 methods within this class:
* Each method is called within `UserInput` class
1. ***Validating Library ID:***
    - `check_library_id(self, library_id)`
    - Checks Library ID if it matched the REGEX pattern 
        * `self.id_pattern` (**[LID-(digits)]**)
2. ***Formatting Library ID:***
    - `format_library_id(self, library_id)`
    - Finds all string elements that match REGEX patterns, joins them, and assigns to a variable
        * `self.letters` (**[a-zA-Z]**)
        * `self.numbers` (**[0-9]**)
    - Capitalizes the letters, then concatenates `letters` + '-' + `numbers`, and returns the formatted ID
3. ***Validating Publication Date:***
    - `validate_year(self, publication_date)`
    - Checks if the publication date the user provides exists by using the `datetime` built-in module to get today's year
#### *User Inputs:*
* `class UserInput`
* Once instantiated, establishes instances for:
    - `ValidateInputs()`
    - `UniqueIdGenerator()`
        * Discussed further in README under the `User` class section
        * [Module for User & UniqueIdGenerator Classes](user.py)
    - `library` from UserInterface class
* Each method uses `input()` for user input and calls to the appropriate modules, classes, and methods to complete their actions
* There are 8 methods within this class and commented for clarity on which Menus they came from:

**User Operations Inputs:**

1. *Add a New User:*
    - `add_user(self)`
    - Instantiates a method from the `User` class to generate a unique Library ID ensuring no duplicated IDs
        * `self.unique_id_generator.generate_id()`
    - Prompts the user for the new user's name, instantiates the `User` class, and returns a confirmation message with details broken down
        > \*\* New User Added: \*\*
2. *View User Details:*
    - `view_user_details(self)`
    - Prompts the user for Library ID to view details, then validates and formats/revalidates it if needed
        * `self.validate_inputs.check_library_id(library_id)`
        * `self.validate_inputs.format_library_id(library_id)`
    - On failure, the `ValueError` is raised:
        > \* Invalid Library ID. Please try again. \*
    - Otherwise, advises the user of the action, instantiates a method from the `Library` class to find the user's details, and returns the results
        > \* Retrieving Details for Library ID: {library_id}... \*
        * `self.library._find_user_by_library_id(library_id)`

**Book Operations Inputs:**

3. *Add a New Book:*
    - `add_book(self)`
    - Prompts the user to enter title, author, genre, and publication date for the new book
    - Validates the publication date ensuring the year already exists
        * `self.validate_inputs.validate_year(publication_date)`
    - If it fails validation, the `ValueError` is raised:
        > \* '{publication_date}' is not a valid publication year. Please try again. \*
    - If pass, instantiates `Book` class with the details, calls to `Library` class for `add_book_to_library(book)` method, and provides the user with a confirmation message along with details broken down
    - If the author is a *NEW* author, calls `add_author(author)` method
4. *Borrow a Book:*
    - `borrow_book(self)`
    - Prompts the user for title of the book to borrow and checks if it exists and if it is available by calling methods within `Book` class
        * `if book in self.library.books`
        * `self.library.books[book].get_availability() == "Available"`
    - If it doesn't pass, `LookupError` is raised:
        > \* Book not available or not found. \*
    - When it does pass, the user is prompted for Library ID which is then validated and formatted/revalidated if needed
        * `self.validate_inputs.check_library_id(library_id)`
        * `self.validate_inputs.format_library_id(library_id)`
    - On failure, `ValueError` is raised:
        > \* Invalid Library ID. Please try again. \*
    - Otherwise, it instantiates a method from the `Library` class to add the book to the user's borrowed books list, marks it as 'Borrowed' in the library, and returns the results
5. *Return a Book:*
    - `return_book(self)`
    - Prompts the user for title of the book to return and their Library ID, which is then validated and formatted/revalidated if needed
        * `self.validate_inputs.check_library_id(library_id)`
        * `self.validate_inputs.format_library_id(library_id)`
    - On failure, `ValueError` is raised:
        > \* Invalid Library ID. Please try again. \*
    - Otherwise, it instantiates a method from the `Library` class to remove the returned book from the user's borrowed books list, marks it as available in the library, and returns the results
6. *Search for a Book:*
    - `search_for_book(self)`
    - Prompts the user for title of the book to search for and advises the user of the action:
        > \* Searching for {title} in Library... \*
    - Then, instantiates a method from the `Library` class to find the book details within the Library and returns the results
        * `self.library.find_book_by_title(book)`

**Author Operations Inputs:**

7. *Add a New Author:*
    - `add_author(self, author=None)`
    - This has a default value for `author` in case it is being called from another method has an author variable already
    - If no author has been provided, the user is prompted for the author's name
    - After author has been collected, the user is prompted for the author's biography
    - Then, the `Author` class is instantiated with the author's details, calls to `Library` class method to add the author to library, and provides the user with a confirmation message with details broken down
        * `self.library.add_author_to_library(author)`
        > \*\* New Author Added: \*\*
8. *View Author Details:*
    - `view_author_details(self)`
    - Prompts the user for the author's name and advises of the action
        > \* Retrieving Details for Author: {author}... \*
    - Then instantiates a method from the `Library` class and returns the results
        * `self.library.find_author(author)`

### Library Class & Methods
* [Module for Library Class & Methods](library.py)
* This module handles the `Library` class which contains the Library's dictionaries of users, books, and authors as well as any actions associated
* There are 11 methods within this class:

1. ***Add User to Library***
    - `add_user_to_library(self, user)`
    - Takes the class object `user` and adds it to the users dictionary
2. ***Add Borowed Book***
    - `add_borrowed_book(self, library_id, title)`
    - Appends the book to the user's `_borrowed_books` list
    - Marks the book as `"Borrowed"` in the books dictionary
    - Returns a confirmation message
3. ***Remove Returned Book***
    - `remove_returned_book(self, library_id, title)`
    - Removes the book from the user's `_borrowed_books` list
    - Marks the book as `"Available"` in the books dictionary
    - Returns a confirmation message
4. ***Find User by Library ID***
    - `_find_user_by_library_id(self, library_id)`
    - Finds the user by their Library ID and calls a method from the user class for formatting and printing of details
    - If not found, `LookupError` is raised:
        > `f"Cannot find user with Library ID: {library_id}`
5. ***Display All Users***
    - `display_all_users(self)`
    - Calls a method from the `User` class to get the user's name and prints each user's Library ID & Name
6. ***Add Book to Library***
    - `add_book_to_library(self, book)`
    - Takes the class object `book` and adds it to the users dictionary
7. ***Find Book by Title***
    - `find_book_by_title(self, book)`
    - Finds the book by title and calls a method from the book class for formatting and returning details
    - If not found, `LookupError` is raised:
        > `f"Cannot find book with title: {book}`
8. ***Display All Books***
    - `display_all_books(self)`
    - Calls a method from the `Book` class for formatting and returning all book's details
9. ***Add Author to Library***
    - `add_author_to_library(self, author)`
    - Takes the class object `author` and adds it to the users dictionary
10. ***Find Author***
    - `find_author(self, author_name)`
    - Finds the author by name and calls a method from the author class for formatting and returning details
    - If not found, `LookupError` is raised:
        > `f"Cannot find author: {author_name}`
11. ***Display All Authors***
    - `display_all_authors(self)`
    - Prints each author in a list

### User & UniqueIdGenerator Classes
* [Module for User & UniqueIdGenerator Classes and Methods](user.py)
* This module handles all users data
* There are 2 classes with their own methods:
    - **UniqueIdGenerator**
    - **User**
#### *Unique ID Generation:*
* `class UniqueIdGenerator`
* Once instantiated, establishes instances for:
    - `self.counter = 0`
    - `self.prefix = 'LID-'`
        * These are both used within the second method
* *Library ID Generator:*
    - `generate_id(self)`
    - Increments the counter, concatenates it to the prefix, and returns the value
        * `{self.prefix}{self.counter}`
#### *User:*
* `class User`
* Once instantiated, establishes instances for user's data inputs including:
    - Library ID (private attribute)
    - Name (private attribute)
    - Defaulted empty list for borrowed books (private attribute)
* There are 6 methods within this class including:

1. *Library ID Getter:*
    - `get_library_id(self)`
    - Gets the private attribute for any use outside of the Class
2. *Name Getter*
    - `get_name(self)`
    - Gets the private attribute for any use outside of the Class
3. *Borrowed Books Getter*
    - `get_borrowed_books(self)`
    - Gets the private attribute for any use outside of the Class
4. *Assign Borrowed Book to User Data*
    - `add_borrowed_book(self, book)`
    - Appends the book title to the user's borrowed book list
5. *Remove a Returned Book from User Data*
    - `return_borrowed_book(self, book)`
    - Finds the book title within the user's "Borrowed Books" list and removes it from the list
6. *Format User*
    - `format_user(self)`
    - Formats the user's data to show Library ID, Name, and each (if any) Borrowed books

### Book Class & Methods
* [Module for Book Class & Methods](book.py)
* This module handles the `Book` class and it's own methods
* There are 7 methods within this class:
1. *Title Getter*
    - `get_title(self)`
2. *Author Getter*
    - `get_author(self)`
3. *Genre Getter*
    - `get_genre(self)`
4. *Publication Date Getter*
    - `get_publication_date(self)`
5. *Availability Getter*
    - `get_availability(self)`
6. *Marking Book's Availability*
    - `mark_as_borrowed(self, is_borrowed)`
    - If `is_borrowed` is True, marks `availability` as `"Borrowed"`
    - If `is_borrowed` is False, marks `availability` as `"Available"`
7. *Format Book*
    - `format_book(self)`
    - Formats the book's details

### Author Class & Methods
* [Module for Author Class & Methods](author.py)
* This module handles the `Author` class and methods
* There are 3 methods within this class:
1. *Author Name Getter*
    - `get_author_name(self)`
2. *Biography Getter*
    - `get_biography(self)`
3. *Format Author*
    - `format_author(self)`
    - Formats the author's details
