
class Book:
    def __init__(self,isbn,title,autor,date_publication,genre,available_copies,state):
        self.isbn = isbn
        self.title = title
        self.autor = autor
        self.date_publication = date_publication
        self.genre = genre
        self.available_copies = available_copies
        self.state = state

    def show_book_info(self):
        print("======= Book Information ======")
        print(f"Title: {self.title}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Genre: {self.genre}")
    
    def update_book_state(self):
        print("======= Book ======")
        search_book = input ("Type book's ISBN or Title to update:_ ")
        print (f"looking book by: {search_book}")
    
    def validate_book_availability(self):
        print("======= Book ======")
        book_availability = input ("Type book's ISBN or Title (availability):_ ")
        print(f"availability: {self.available_copies}")



myclas = Book(564,"title","michel","02/1/2025","horror",6,"avaiable")

myclas.show_book_info()
myclas.update_book_state()