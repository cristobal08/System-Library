from lightdb import LightDB
from lightdb.models import Model

# Initialize the database
db_user = LightDB("src/data/users.json")

# Define a User model
class UserRecord(Model, table="user_general"):
    user_type: str
    user_name: str
    user_last_name: str
    address: str
    age: int
    major: str  
    semester: int
    department: str
    specialty: str