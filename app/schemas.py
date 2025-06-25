from pydantic import BaseModel,ConfigDict,EmailStr
from pydantic.types import conint
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at : datetime
    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(Post):
    id:int
    created_at: datetime
    user_id :int
    owner: UserResponse
    model_config = ConfigDict(from_attributes=True)

class PostWithVotes(BaseModel):
    Post: PostResponse
    votes: int

class Token(BaseModel):
    access_token :str
    token_type : str

class TokenData(BaseModel):
    id:Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)