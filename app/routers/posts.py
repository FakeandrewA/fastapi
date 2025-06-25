#fastapi
from fastapi import Response,status,HTTPException,Depends,APIRouter


#validation
from typing import List,Optional
from .. import schemas

#ORM
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import models,oauth2
from ..database import get_db

router = APIRouter(prefix="/posts",tags=["posts"])

#/posts
@router.get("/",response_model=List[schemas.PostWithVotes])
def get_posts(db: Session = Depends(get_db),current_user:models.User = Depends(oauth2.get_current_user),
              limit:int = 10,skip:int = 0,search:Optional[str] = ""):
    # cursor.execute("""SELECT * from posts""")
    # posts = cursor.fetchall()
    print(limit)
    posts = db.query(models.Post)
    
    results = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit=limit).offset(offset=skip).all()

    print(results)
    return results

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_posts(post: schemas.PostCreate, db:Session = Depends(get_db),current_user:models.User = Depends(oauth2.get_current_user)):
    # cursor.execute("INSERT INTO posts (title,content,published) Values(%s,%s,%s) Returning *",(post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    
    # new_post = models.Post(title=post.title,content=post.content,published=post.published)
    dict_post = post.model_dump()
    dict_post["user_id"] = current_user.id 
    new_post = models.Post(**dict_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    print(type(new_post))
    return new_post

@router.get("/{id}",response_model=schemas.PostWithVotes)
def get_post(id: int,db: Session = Depends(get_db),current_user:models.User= Depends(oauth2.get_current_user)):
    # cursor.execute("select * from posts where id = %s",str(id))
    # p = cursor.fetchone()
    # # print(p)
    print("hello")
    p = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    print(p)
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message":f"post with id {id} was not found"}
    if p[0].user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")
    
    return p

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db),current_user:models.User = Depends(oauth2.get_current_user)):

    # cursor.execute("DELETE from posts where id = %s returning *",str(id))
    # deleted_post = cursor.fetchone()
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    if not deleted_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with id {id} was not found.")
    
    if deleted_post.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")
    # conn.commit()
    deleted_post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@router.put("/{id}",response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db),current_user:models.User = Depends(oauth2.get_current_user)):

    # cursor.execute("update posts set title = %s , content = %s , published = %s where id = %s returning *",(post.title,post.content,post.published,str(id)))
    # updated_post = cursor.fetchone()
    updated_post = db.query(models.Post).filter(models.Post.id == id)
    
    post1 = updated_post

    if not post1.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with id {id} was not found.")
    
    if post1.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")
    
    updated_post.update( post.model_dump() ,synchronize_session=False)
    db.commit()
    return updated_post.first()
