
#fastapi
from fastapi import status,HTTPException,Depends ,APIRouter


#validation
from .. import schemas

#ORM
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db

#hash
from ..util import hash


router = APIRouter(prefix="/users",tags=["users"])

#/users
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate , db:Session = Depends(get_db)):

    #hasing
    user.password = hash(user.password)

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(type(new_user))
    return new_user

@router.get("/{id}",response_model=schemas.UserResponse)
def get_user(id: int , db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
