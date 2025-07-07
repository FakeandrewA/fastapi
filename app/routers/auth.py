from fastapi import APIRouter,Depends,status,HTTPException,Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import UserLogin,Token
from .. import models
from ..util import verify
from ..oauth2 import create_access_token

router = APIRouter(tags=["Authentication"])

@router.post("/login",response_model=Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db: Session=Depends(get_db)):

    #username
    #password

    user:models.User = db.query(models.User).filter(models.User.email==user_credentials.username).first()
    # print(user.id)
    if user:
        if verify(user_credentials.password,user.password):
            #create a token and return 
            access_token = create_access_token(data={"user_id":user.id})
            return {"access_token":access_token,"token_type":"bearer"}
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
        
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")


