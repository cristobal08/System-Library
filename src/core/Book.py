from utils.DbLibrary import BookInfo

class Book:
    def __init__(self,isbn= None, title= None, autor= None, available_copies= None, state= None):
        self.isbn = isbn
        self.title = title
        self.autor = autor
        self.available_copies = available_copies
        self.state = state
    
    def add_book(self):
        book_info = {}

        book_info["isbn"] = input("ISBN Book: ")
        book_info["title"] = input("Book Title: ")
        book_info["autor"] = input("Autor: ") 
        book_info["available_copies"] = int(input("Number of copies avaibles: "))
        book_info["state"] =  input("Book state on rent/no aviable/ avaible: ")

        return book_info
    
    def save_book(self,book_data):
        BookInfo.create(**book_data)
    
    def remove_book(self,book_title):
        rm_book = self.find_book(book_title)

        if rm_book:
            print(f"Deleting book:  {rm_book.title}")
            rm_book.delete()
        else:
            print("Book Not found in system")
    
    def find_book(self, book_title):
        try:
            return BookInfo.get(BookInfo.title == book_title)
        except:
            return None


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