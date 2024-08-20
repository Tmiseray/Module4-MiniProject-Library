class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = "Available"
    
    def get_title(self):
        return self.title

    def get_availability(self):
        return self.availability
    
    def mark_as_borrowed(self, is_borrowed):
        if is_borrowed:
            self.availability = "Borrowed"
        else:
            self.availability = "Available"
