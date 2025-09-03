from lightdb import LightDB
from lightdb.models import Model

# Initialize the database
db_library = LightDB("src/data/library.json")

class UserStudent(Model, table="StudentInfo", database=db_library):
    user_type: str
    user_name: str
    user_last_name: str
    address: str
    age: int
    major: str  
    semester: int

class UserTeacher(Model, table="TeacherInfo", database=db_library):
    user_type: str
    user_name: str
    user_last_name: str
    address: str
    age: int
    department: str
    specialty: str

class BookInfo(Model, table="BookInfo", database=db_library):
    isbn: str
    title: str
    autor: str
    available_copies: int
    state: str