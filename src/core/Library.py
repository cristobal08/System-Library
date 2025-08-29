from core.User import User
from core.Book import Book

class Library:

    def __init__(self):
        self.user = User()
        self.book = Book()

    def menu(self):
        
        try:
            print("\n--- Library System Menu --- \n")
            print("1: add user: ")
            print("2: remove user: ")
            print("3: uptade user: ")

            print("\n--- Books options --- \n")
            print("4: add book: ")
            print("5: remove book: ")
            print("6: uptade book: ")

            option_registry = int(input("Chose option for user: "))

            match option_registry:
                case 1:
                    print("\n Fill the information , write N/A if perfil dont apply \n")
                    data = self.user.create_user()
                    self.user.save_info_user(data)
                case 2:
                    print(" \n Removing user from system \n")
                    self.user.remove_user()
                case 3:
                    print("\n Update information User \n")
                    self.user.update_user()
                case 4:
                    print("Please , type the book information")
                    book_data = self.book.add_book()
                    self.book.save_book(book_data)

        
        except ValueError:
            print(" choose an option !!!")