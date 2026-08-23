from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str


user = User(id=1, name='Alice', email='bdvfd@example.com')
