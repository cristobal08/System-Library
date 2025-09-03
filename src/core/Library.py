from core.User import User
from core.Book import Book

class Library:

    def __init__(self):
        self.user = User()
        self.book = Book()

    def menu(self):
        while True:
            try:
                print("\n--- Library System Menu --- \n")
                print("1: add user: ")
                print("2: remove user: ")
                print("3: update user: ")
                print("\n--- Books options --- \n")
                print("4: add book: ")
                print("5: remove book: ")
                print("6: update book: ")
                print("\n Circulation (Library loans)")
                print("7: Book lending: ")
                print("8: EXIT")

                option_registry = int(input("Choose option: "))

                match option_registry:
                    case 1:
                        print("\n Fill the information...")
                        data = self.user.create_user()
                        self.user.save_info_user(data)
                    case 2:
                        print(" \n Removing user from system \n")
                        self.user.remove_user()
                    case 3:
                        print("\n Update information User \n")
                        self.user.update_user()
                    case 4:
                        print("Please, type the book information")
                        book_data = self.book.add_book()
                        self.book.save_book(book_data)
                    case 5:
                        book_title = input("Book title to be removed: ")
                        self.book.remove_book(book_title)
                    case 6:
                        self.book.update_book_info()

                    case 8:
                        print("Closing System!")
                        break 
                    case _:
                        print("Invalid option!")
                
                input("\nPress ENTER to continue...")
            except ValueError:
                print(" choose an option !!!")