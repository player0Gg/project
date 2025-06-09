from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database
from model.tenders import Tender
from schema.tenders import Tender_create, Tender_update
from router.login import get_current_user
from model.users import Users
from utils.save_files import save_file
from func.tenders import show_tender, create_tender, update_tender, delete_tender

tenders_router = APIRouter(tags=["Tenders"])

@tenders_router.get("/tenders_get")
def tenders_get(ident: int = None, db: Session = Depends(database)):
    return show_tender(ident, db)

@tenders_router.post("/tenders_create")
def tenders_create(tender: Tender_create, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return create_tender(tender, current_user, db)

@tenders_router.put("/tenders_update")
def tenders_update(ident: int, tender: Tender_update, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return update_tender(ident, tender, current_user, db)

@tenders_router.put("/tenders_images")
def tenders_images(ident: int, image: str, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    if current_user.role != "admin":
        return {"error": "You are not admin"}
    
    tender = db.query(Tender).filter(Tender.id == ident).first()
    if not tender:
        return {"error": "Tender not found"}
    
    tender.image = save_file(image)
    db.commit()
    return {"message": "Image updated successfully"}

@tenders_router.put("/tenders_files")
def tenders_files(ident: int, files_tender: str, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    if current_user.role != "admin":
        return {"error": "You are not admin"}
    
    tender = db.query(Tender).filter(Tender.id == ident).first()
    if not tender:
        return {"error": "Tender not found"}
    
    tender.files_tender = save_file(files_tender)
    db.commit()
    return {"message": "Files updated successfully"}

@tenders_router.delete("/tenders_delete")
def tenders_delete(ident: int, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return delete_tender(ident, current_user, db)