class User:
    def __init__(self,name,last_name,address,book_historic):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.book_historic = book_historic
    
    def request_book(self):
        print("======= Request Book =======")
        search_book = input("Type book's ISBN or Title:_ ")

        if search_book != 0:
            print(f"Book {search_book} ")
        else:
            print(f"Book {search_book} not Avaiable")

    def return_book(self):
        print("======= Return Book =======")
        return_book = input("What's book's ISBN or Title:_ ")
        print(f"Book {return_book} is returned")
