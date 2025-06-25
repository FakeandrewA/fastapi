from fastapi import FastAPI,status,Response,HTTPException,Depends

import psycopg2
from psycopg2.extras import RealDictCursor
import time

from .schema import CreateProduct,UpdateProduct

from sqlalchemy.orm import Session

from . import models
from .database import engine,SessionLocal,get_db

models.Base.metadata.create_all(bind=engine)

# while True:
#     try:
#         conn = psycopg2.connect(host="localhost",database="fastapi",user="postgres",password="andrew",cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("DataBase Connection Successful")
#         break
#     except Exception as e:
#         print(e)


app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello Welcome to the API"}

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    # cursor.execute("SELECT * from posts2")
    # posts = cursor.fetchall()
    posts = db.query(models.Products).all()
    if posts:
        return posts
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.get("/products/{id}")
def get_product(id:int,db:Session = Depends(get_db)):
    # cursor.execute("SELECT * FROM posts2 WHERE id = %s",(str(id),))
    # post = cursor.fetchone()
    post = db.query(models.Products).filter(models.Products.id == id).first()
    if post:
        return post
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.post("/products")
def create_product(product:CreateProduct,db:Session=Depends(get_db)):
    # productName = product.name
    # productPrice = product.price
    # cursor.execute("INSERT INTO posts2 (name,price) values(%s,%s) returning *",(productName,productPrice))
    # new_product = cursor.fetchone()

    # conn.commit()
    new_product = models.Products(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.delete("/products/{id}")
def delete_product(id:int,db:Session = Depends(get_db)):
    # cursor.execute("DELETE FROM posts2 WHERE id = %s RETURNING *",str(id))
    # deleted_product = cursor.fetchone()
    deleted_product = db.query(models.Products).filter(models.Products.id == id)
    if deleted_product.first():
        deleted_product.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.put("/products/{id}")
def update_product(id:int,product:UpdateProduct,db:Session = Depends(get_db)):
    # new_name = product.name
    # new_price = product.price
    # cursor.execute("UPDATE posts2 SET name = %s , price = %s WHERE id = %s RETURNING *",(new_name,new_price,str(id)))
    # updated_product = cursor.fetchone()
    updated_product = db.query(models.Products).filter(models.Products.id == id)
    if updated_product.first():
        # conn.commit()
        updated_product.update(product.model_dump(),synchronize_session=False)
        db.commit()
        return updated_product.first()
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)    
    
    


