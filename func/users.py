from model.users import Users
from schema.users import User_create, User_update, Admin_create, Admin_update
from db import database
from router.login import get_password_hash

def get_user_by_id(user_id: int, db: database):
    user = db.query(Users).filter(Users.id == user_id).first()
    db.close()
    return user

def create_user(user: User_create, db: database):
    new_user=Users(
        name=user.name,
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
        role='user'  # Default role for regular users
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return {'massage': 'User created successfully'}

def update_user(user_id: int, user: User_update, db: database):
    db.query(Users).filter(Users.id == user_id).update({
        Users.name: user.name,
        Users.username: user.username,
        Users.email: user.email,
        Users.password: get_password_hash(user.password)
    })
    db.commit()
    db.close()
    return {'massage': 'User updated successfully'}

def delete_user(user_id: int, db: database):
    db.query(Users).filter(Users.id == user_id).delete()
    db.commit()
    db.close()
    return {'massage': 'User deleted successfully'}

#-----------------------------------------admin-----------------------------------------

def get_all(current_user, db: database):
    if current_user.role != 'admin':
        raise Exception("You do not an admin")
    else:
        user = db.query(Users).all()
        db.close()
        return user

def create_for_admin(user: Admin_create, current_user, db: database):
    if current_user.role != 'admin':
        raise Exception("You do not an admin")
    else:
        new_user=Users(
            name=user.name,
            username=user.username,
            email=user.email,
            password=get_password_hash(user.password),
            role=user.role
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        db.close()
        return {'massage': 'User created successfully'}

def update_for_admin(user_id: int, user: Admin_update,current_user, db: database):
    if current_user.role != 'admin':
        raise Exception("You do not an admin")
    else:
        db.query(Users).filter(Users.id == user_id).update({
            Users.name: user.name,
            Users.username: user.username,
            Users.email: user.email,
            Users.password: get_password_hash(user.password),
            Users.role: user.role
        })
        db.commit()
        db.close()
        return {'massage': 'User updated successfully'}

def delete_for_admin(user_id: int, current_user, db: database):
    if current_user.role != 'admin':
        raise Exception("You do not an admin")
    else:
        db.query(Users).filter(Users.id == user_id).delete()
        db.commit()
        db.close()
        return {'massage': 'User deleted successfully'}