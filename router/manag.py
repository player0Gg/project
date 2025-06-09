from fastapi import APIRouter, Depends, UploadFile
from db import database
from model.manag import Manag
from schema.manag import Manag_create, Manag_update
from sqlalchemy.orm import Session
from model.users import Users
from utils.save_files import save_file
from router.login import get_current_user
from func.manag import get_manag, create_manag, update_manag, delete_manag

manag_router = APIRouter(tags=["Management"])

@manag_router.get("/management_get")
def management_get(ident: int = None, db: Session = Depends(database)):
    return get_manag(ident, db)

@manag_router.post("/management_create")
def management_create(manag: Manag_create, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return create_manag(manag, current_user, db)

@manag_router.put("/management_update")
def management_update(ident: int, manag: Manag_update, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return update_manag(ident, manag, current_user, db)

@manag_router.put("/management_image")
def management_image(ident:int, file: UploadFile, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    if current_user.role != "admin":
        return {"error": "You do not have permission to perform this action."}
    
    manag = db.query(Manag).filter(Manag.id == ident).first()
    if not manag:
        return {"error": "Management member not found."}
    manag.image = save_file(file)
    db.commit()
    return {"message": "Image updated successfully."}

@manag_router.delete("/management_delete")
def management_delete(ident: int, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return delete_manag(ident, current_user, db)