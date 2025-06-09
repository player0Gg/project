from model.tenders import Tender
from schema.tenders import Tender_create, Tender_update

def show_tender(ident:int, db):
    if ident is None:
        return db.query(Tender).all()
    else:
        return db.query(Tender).filter(Tender.id == ident).first()

def create_tender(tender: Tender_create, current_user, db):
    if current_user.role!="admin":
        return {"error": "Unauthorized access"}
    new_tender = Tender(
        text=tender.text,
        image=None,  # Assuming image handling is done separately
        files_tender=None  # Assuming files handling is done separately
    )
    db.add(new_tender)
    db.commit()
    return {"message": "Tender created successfully", "id": new_tender.id}

def update_tender(ident: int, tender: Tender_update, current_user, db):
    if current_user.role!="admin":
        return {"error": "Unauthorized access"}
    else:
        if not db.query(Tender).filter(Tender.id == ident).first():
            return {"error": "Tender not found"}
        else:
            db.query(Tender).filter(Tender.id == ident).update({
                Tender.text: tender.text,
                })
    
            db.commit()
            return {"message": "Tender updated successfully"}
        
def delete_tender(ident: int, current_user, db):
    if current_user.role!="admin":
        return {"error": "Unauthorized access"}
    else:
        tender = db.query(Tender).filter(Tender.id == ident).first()
        if not tender:
            return {"error": "Tender not found"}
        else:
            db.delete(tender)
            db.commit()
            return {"message": "Tender deleted successfully"}
