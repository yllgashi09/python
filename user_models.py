from pydantic import Basemodel, conint, constr
from typing import optional
class user(Basemodel):
    id: int
    name: str
    age: optional[int] = None
    email: optional[str] = None

user1 = User(id=1, name='john', age=25,email='john@example.com')

user2 = User(id=1, name='john', age=25)

user3 = User(id=1, name='john',email='john@example.com')
print(user3)

class user(Basemodel):
    id : conint(gt=0)
    name: constr(min_length=2, max_length=50)

valid_user = another_user(id=1, name='john')
print(valid_user)

valid_user1 = another_user(id=0, name='john')
print(valid_user1)