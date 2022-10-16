from fastapi import status, HTTPException

from .. import models, schemas
from sqlalchemy.orm import Session


# GET ALL POSTS
def get_all(db: Session):
    Blog = models.Blog
    blogs = db.query(Blog).all()

    return blogs


# CREATE POST
def create(request: schemas.Blog, db: Session):
    # define model variables
    Blog = models.Blog

    # logic
    new_blog = Blog(title=request.title, body=request.body)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


# DELETE POST
def delete(id: int, db: Session):
    Blog = models.Blog

    db.query(Blog).filter(Blog.id == id).delete(synchronize_session=False)
    db.commit()

    return {'msg': 'Post deleted!'}


# UPDATE POST
def update(id: int, request: schemas.Blog, db: Session):
    Blog = models.Blog

    post = db.query(Blog).filter(Blog.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist!")
    else:
        post.update(request.dict())
        db.commit()

    return {'msg': 'Updated!'}


# GET POST
def get_post(id: int, db: Session):
    # define model variables
    Blog = models.Blog

    # logic
    post = db.query(Blog).filter(Blog.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} does not exist.")

        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id {id} does not exist.'}

    return post
