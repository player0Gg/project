from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from db import database
from model.ceremony import Ceremony
from schema.ceremony import Ceremony_create, Ceremony_update
from router.login import get_current_user
from model.users import Users
from utils.save_files import save_file
from func.ceremony import show_ceremony, create_ceremony, update_ceremony, delete_ceremony

ceremony_router = APIRouter(tags=["Ceremonies"])

@ceremony_router.get("/ceremonies_get")
def ceremonies_get(ident: int = None, db: Session = Depends(database)):
    return show_ceremony(ident, db)

@ceremony_router.post("/ceremonies_create")
def ceremonies_create(ceremony: Ceremony_create, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return create_ceremony(ceremony, current_user, db)

@ceremony_router.put("/ceremonies_update")
def ceremonies_update(ident: int, ceremony: Ceremony_update, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return update_ceremony(ident, ceremony, current_user, db)

@ceremony_router.put("/ceremonies_images")
def ceremony_images(ident:int, image: UploadFile, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    if current_user.role != "admin":
        return {"error": "You are not admin"}
    
    ceremony = db.query(Ceremony).filter(Ceremony.id == ident).first()
    if not ceremony:
        return {"error": "Ceremony not found"}
    
    ceremony.image = save_file(image)
    db.commit()
    return {"message": "Image updated successfully"}

@ceremony_router.delete("/ceremonies_delete")
def ceremonies_delete(ident: int, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return delete_ceremony(ident, current_user, db)