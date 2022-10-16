from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, oauth2
from ..database import *
from ..repository import blog

# DEFINE ROUTER
router = APIRouter(
    prefix="/blog",
    tags=['Blog']
)


# ALL POSTS ROUTE
@router.get('/', response_model=List[schemas.ShowBlog])
def all_posts(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


# CREATE POST ROUTE
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


# DELETE POST ROUTE
@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_post(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)


# UPDATE POST ROUTE
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_post(id, request: schemas.Blog, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


# GET POST ROUTE
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_post(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_post(id, db)
