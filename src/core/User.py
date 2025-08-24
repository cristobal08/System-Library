from utils.Db import UserRecord


class User:
    # def __init__(self):
    #     self.save_user = UserInfo()
    
    def create_user(self):
        
        print("\n Fill the information , write N/A if perfil dont apply \n")
        self.user_type = input("Type on user \"Student or Teacher\" ")
        self.user_name = input("user name: ")
        self.user_last_name = input("user last name: ")
        self.address = input ("user address: ")
        self.age = int(input("age: "))
        self.major = input("what's the major?: ")
        self.semester = int(input("current semester?: "))
        self.department = input("department: ")
        self.specialty = input("specialty: ")

        UserRecord.create(user_type = self.user_type, 
                        user_name = self.user_name,
                        user_last_name = self.user_last_name,
                        address = self.address,
                        age = self.age,
                        major = self.major,
                        semester = self.semester,
                        department = self.department,
                        specialty = self.specialty)
        
    def remove_user(self):

        print(" \n Removing user from system \n")

        self.rm_user = input("User's name to be removed:  ")
        retrieved_user =  UserRecord.get(UserRecord.user_name == self.rm_user)
        
        if retrieved_user:
            print("User found, Deleting info! ")
            retrieved_user.delete()
        else:
            print("user Not found in system")
            


        

#     def request_book(self):
#         print("======= Request Book =======")
#         search_book = input("Type book's ISBN or Title:_ ")

#         if search_book != 0:
#             print(f"Book {search_book} ")
#         else:
#             print(f"Book {search_book} not Avaiable")

#     def return_book(self):
#         print("======= Return Book =======")
#         return_book = input("What's book's ISBN or Title:_ ")
#         print(f"Book {return_book} is returned")

# class Studen(User):
#     def __init__(self, type, major, semester):
#         self.type = type
#         self.major = major
#         self.semester = semester

#     def limit_book(self):
#         print("-------  search number of books allowed ---------")


# class Teacher(User):
#     def __init__(self, department, specialty):
#         self.department = department
#         self.specialty = specialty

#     def extend_rent(self):
#         print("-------  extended loan duration ---------")



