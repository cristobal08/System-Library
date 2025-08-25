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
                    print("\n Fill the information , write N/A if perfil dont apply \n")
                    data = self.user.create_user()
                    self.user.save_info_user(data)
                case 2:
                    print(" \n Removing user from system \n")
                    self.user.remove_user()
                case 3:
                    print("\n Update information User \n")
                    self.user.update_user()
        except ValueError:
            print(" choose an option !!!")