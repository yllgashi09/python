from pydantic import Basemodel, FieldserializationInfo, Field_validator, conint, constr

class user(Basemodel):
    id: int
    name: str
    age: int

    @field_validator('age')
    def age_must_be_pozitive(cls, v, info: FieldserializationInfo):
        if v <= 0:
            raise ValueError('Age must be pozitive')
        return v
try:
    user = User(id=1, name="john", age= -1)
    print(user)
except ValueError as e:
    print(e)

class Address(Basemodel):
    street: str
    city: str

class Users(BaseModel):
    id : int
    name: str
    address: Address