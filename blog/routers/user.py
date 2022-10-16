from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, oauth2
from ..database import *
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['User']
)


# CREATE USER ROUTE
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


# GET USER ROUTE
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.get_user(id, db)
