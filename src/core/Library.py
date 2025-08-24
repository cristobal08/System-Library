from core.User import User

class Library:

    def __init__(self):
        self.user = User()

    def menu(self):
        
        try:
            print("\n--- Library System Menu --- \n")
            print("1: add user: ")
            print("2: remove user: ")
            print("3: uptade user: ")

            option_registry = int(input("Chose option for user: "))

            match option_registry:
                case 1:
                    self.user.create_user()
                case 2:                    
                    self.user.remove_user()
                case 3:                    
                    self.user.update_user()
        except ValueError:
            print(" choose an option !!!")