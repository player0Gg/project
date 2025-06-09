from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from db import database
from model.users import Users
from schema.users import User_create, User_update, Admin_create, Admin_update
from schema.tokens import TokenData, Token
from router.login import get_current_user
from func.users import get_user_by_id, create_user, update_user, delete_user, get_all, create_for_admin, update_for_admin, delete_for_admin

users_router=APIRouter(tags=['Users'])

@users_router.get('/users_get')
def get_user(user_id: int, db: Session = Depends(database)):
    return get_user_by_id(user_id, db)

@users_router.post('/users_create')
def create_new_user(user: User_create, db: Session = Depends(database)):
    return create_user(user, db)

@users_router.put('/users_update')
def update_existing_user(user_id: int, user: User_update, db: Session = Depends(database)):
    return update_user(user_id, user, db)

@users_router.delete('/users_delete')
def delete_existing_user(user_id: int, db: Session = Depends(database)):
    return delete_user(user_id, db)

#-----------------------------------------admin-----------------------------------------
@users_router.get('/admin_get_all')
def get_all_users(current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return get_all(current_user.id, current_user, db)

@users_router.post('/admin_create')
def create_user_for_admin(user: Admin_create, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return create_for_admin(user, current_user, db)

@users_router.put('/admin_update')
def update_user_for_admin(user_id: int, user: Admin_update, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return update_for_admin(user_id, user, current_user, db)

@users_router.delete('/admin_delete')
def delete_user_for_admin(user_id: int, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return delete_for_admin(user_id, current_user, db)
