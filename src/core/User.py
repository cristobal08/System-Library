from utils.DbLibrary import UserStudent, UserTeacher


class User:
    
    def __init__(self, user_type=None, user_name=None, user_last_name=None, 
                address=None, age=None, major=None, semester=None, 
                department=None, specialty=None):
        
        self.user_type = user_type
        self.user_name = user_name
        self.user_last_name = user_last_name
        self.address = address
        self.age = age
        self.major = major
        self.semester = semester
        self.department = department
        self.specialty = specialty

    def create_user(self):

        user_info = {}

        user_info["user_type"] = input("Type on user \"Student or Teacher\" ")
        user_info["user_name"] = input("user name: ")
        user_info["user_last_name"] = input("user last name: ")
        user_info["address"] = input ("user address: ")
        user_info["age"] = int(input("age: "))
        if user_info["user_type"] == "student":
            user_info["major"] = input("what's the major?: ")
            user_info["semester"] = int(input("current semester?: "))
        elif user_info["user_type"] == "teacher":
            user_info["department"] = input("department: ")
            user_info["specialty"] = input("specialty: ")

        return user_info

    def save_info_user(self,data):
        
        if data["user_type"] == "student":
            # operator ** unpacks the key-value pairs of dictionary e.g 
            # {'user_type': 'Student','user_name': 'Juan','age': 20}
            UserStudent.create(**data) 
        elif data["user_type"] == "teacher":
            UserTeacher.create(**data)

    def remove_user(self):

        self.rm_user = input("User's name to be removed:  ")
        retrieved_user = self.find_user(self.rm_user)
        
        if retrieved_user:
            print("User found, Deleting info! ")
            retrieved_user.delete()
        else:
            print("user Not found in system")
    
    def update_user_info(self):
        
        teachers = UserTeacher.all()
        students = UserStudent.all()
        users = teachers + students

        if not users:
            print(" No users in database!")
            return

        print(f"\n All users ({len(users)} total):")
        print("-" * 50)
        for i, user in enumerate(users, 1):
            print(f"{i:2d}. Name: {user.user_name}")
            print(f"     Adress: {user.address} | Type: {user.user_type} ")
        print("-" * 50)

        try:
            choice = int(input("Select user number to update (0 to cancel): "))
            if 1 <= choice <= len(users):
                selected_user = users[choice - 1]
                self.interactive_update(selected_user)
            elif choice == 0:
                print(" Update cancelled")
            else:
                print(" Invalid selection!")
        except ValueError:
            print(" Please enter a valid number!")

    def interactive_update(self, user):
        print("\n Enter new values (press ENTER to keep current):")
        
        new_name = input(f"Name [{user.user_name}]: ").strip()
        if new_name:
            user.user_name = new_name
        
        new_last_name = input(f"last name [{user.user_last_name}]: ").strip()
        if new_last_name:
            user.user_last_name = new_last_name
        
        new_address = input(f"address [{user.address}]: ").strip()
        if new_address:
            user.address = new_address
        
        new_age = input(f"age [{user.age}]: ").strip()
        if new_age:
            new_age = int(new_age)
            user.age = new_age
        
        if user.user_type == "student":
            new_semester = input(f"semester [{user.semester}]: ").strip()
            if new_semester:
                new_semester = int(new_semester)
                user.semester = new_semester
        elif user.user_type == "teacher":
            new_department = input(f"department [{user.department}]: ").strip()
            if new_department:
                user.department = new_department
            new_specialty = input(f"specialty [{user.specialty}]: ").strip()
            if new_specialty:
                user.specialty = new_specialty

        try:
            user.save()
            print("\n User updated successfully!")
        except Exception as e:
            print(f"Error saving changes: {e}")
                

    def find_user(self, name):
        try:
            return UserTeacher.get(UserTeacher.user_name == name)
        except:
            return None



            


        

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



