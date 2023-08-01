from pydantic import ValidationError, BaseModel, PositiveInt
from datetime import datetime

class User(BaseModel):
    id: int  
    name: str = 'John Doe'  
    signup_ts: datetime | None  
    tastes: dict[str, PositiveInt]

external_data = {'id': 1, 'signup_ts': datetime.now(), 'tastes': {'aja': 1}}
try:
    User(**external_data)  
except ValidationError as e:
    print(e.errors())