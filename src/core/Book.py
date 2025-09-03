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
        
    def update_book_info(self):
        books = BookInfo.all()
        
        if not books:
            print(" No books in database!")
            return
        
        print(f"\n All Books ({len(books)} total):")
        print("-" * 50)
        for i, book in enumerate(books, 1):
            print(f"{i:2d}. {book.title} by {book.autor}")
            print(f"     ISBN: {book.isbn} | Copies: {book.available_copies} | State: {book.state}")
        print("-" * 50)
        
        try:
            choice = int(input("Select book number to update (0 to cancel): "))
            if 1 <= choice <= len(books):
                selected_book = books[choice - 1]
                self.interactive_update(selected_book)
            elif choice == 0:
                print(" Update cancelled")
            else:
                print(" Invalid selection!")
        except ValueError:
            print(" Please enter a valid number!")
    
    def interactive_update(self,book):
        
        print(f"\nUpdating: {book.title}")
        print("─" * 40)
        print(f"Current ISBN: {book.isbn}")
        print(f"Current Title: {book.title}")
        print(f"Current Author: {book.autor}")
        print(f"Current Copies: {book.available_copies}")
        print(f"Current State: {book.state}")
        print("─" * 40)
        
        
        confirm = input("Do you want to update this book? (y/n): ").lower()
        if confirm not in ['y', 'yes', 's', 'si']:
            print(" Update cancelled")
            return
        
        
        print("\n Enter new values (press ENTER to keep current):")
        
        # Título
        new_title = input(f"Title [{book.title}]: ").strip()
        if new_title:
            book.title = new_title
        
        # Autor
        new_author = input(f"Author [{book.autor}]: ").strip()
        if new_author:
            book.autor = new_author
        
        # Available copies
        new_copies_str = input(f"Available copies [{book.available_copies}]: ").strip()
        if new_copies_str:
            try:
                new_copies = int(new_copies_str)
                if new_copies >= 0:
                    book.available_copies = new_copies
                else:
                    print(" Copies cannot be negative, keeping current value")
            except ValueError:
                print(" Invalid number, keeping current value")
        
        # Book state
        print(" Valid states: New, Good, Fair, Poor, Damaged")
        new_state = input(f"State [{book.state}]: ").strip()
        if new_state:
            book.state = new_state
        
        try:
            book.save()
            print("\n Book updated successfully!")
            
            # Mostrar información actualizada
            print("\n Updated information:")
            print(f"   Title: {book.title}")
            print(f"   Author: {book.autor}")
            print(f"   Available copies: {book.available_copies}")
            print(f"   State: {book.state}")
        except Exception as e:
            print(f"Error saving changes: {e}")

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