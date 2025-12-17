from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

# Valid input
user = User(name="Alice", age="22", email="alice@example.com")
print(user.age)