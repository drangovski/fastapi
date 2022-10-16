from fastapi import status, HTTPException
from .. import models, schemas, hashing
from sqlalchemy.orm import Session


# CREATE USER
def create_user(request: schemas.User, db: Session):
    User = models.User

    new_user = User(name=request.name, email=request.email, password=hashing.hash_pwd(request.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user(id: int, db: Session):
    User = models.User

    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User does not exist.")
    else:
        return user
