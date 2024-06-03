from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List

import db.db_user as db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# read all users
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# read one user
@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db=db, id=id)


# update user
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    # Handle any exceptions
    return db_user.update_user(db=db, id=id, request=request)


# delete user
@router.get('/{id}/delete')
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db=db, id=id)
