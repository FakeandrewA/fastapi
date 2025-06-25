from sqlalchemy import Column,Integer,String,TIMESTAMP,text
from .database import Base

class Products(Base):
    __tablename__ = "posts2"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))

    