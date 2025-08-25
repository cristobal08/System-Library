from lightdb import LightDB
from lightdb.models import Model

# Initialize the database
db_user = LightDB("src/data/users.json")

class UserStudent(Model, table="UserInfo"):
    user_type: str
    user_name: str
    user_last_name: str
    address: str
    age: int
    major: str  
    semester: int

class UserTeacher(Model, table="UserInfo"):
    user_type: str
    user_name: str
    user_last_name: str
    address: str
    age: int
    department: str
    specialty: str
