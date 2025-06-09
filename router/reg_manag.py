from fastapi import APIRouter, Depends, UploadFile
from db import database
from model.reg_manag import Reg_manag
from sqlalchemy.orm import Session
from schema.reg_manag import Create_regmanag, Update_regmanag
from router.login import get_current_user
from model.users import Users
from func.reg_manag import show_regmanag, add_regmanag, remake_regmanag, remove_regmanag
from utils.save_files import save_file

reg_manag_router = APIRouter(tags=["Region Management"])

@reg_manag_router.get("/regmanag_get")
def get_regmanag(ident:int=None, db: Session=Depends(database)):
    return show_regmanag(ident, db)

@reg_manag_router.post("/regmanag_create")
def create_regmanag(reg_manag:Create_regmanag, current_user:Users=Depends(get_current_user), db: Session=Depends(database)):
    return add_regmanag(reg_manag, current_user, db)

@reg_manag_router.put("/regmanag_update")
def update_regmanag(ident:int, reg_manag: Update_regmanag, current_user:Users=Depends(get_current_user), db: Session=Depends(database)):
    return remake_regmanag(ident, reg_manag,current_user, db)

@reg_manag_router.put("/regmanag_image")
def update_regmanag_image(ident:int, file: UploadFile, db: Session = Depends(database), current_user: Users=Depends(get_current_user)):
    if current_user.role != "admin":
        return {"error": "You are not admin"}
    
    regmanag = db.query(Reg_manag).filter(Reg_manag.id == ident).first()
    if not regmanag:
        return {"error": "Region management not found"}
    
    regmanag.image = save_file(file)
    db.commit()
    return {"message": "Image updated successfully"}

@reg_manag_router.delete("/regmanag_delete")
def delete_regmanag(ident:int, current_user:Users=Depends(get_current_user), db: Session=Depends(database)):
    return remove_regmanag(ident,current_user, db)