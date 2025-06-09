from model.ceremony import Ceremony
from schema.ceremony import Ceremony_create, Ceremony_update

def show_ceremony(ident: int, db):
    if ident is None:
        return db.query(Ceremony).all()
    else:
        return db.query(Ceremony).filter(Ceremony.id == ident).first()
    
def create_ceremony(ceremony: Ceremony_create, current_user, db):
    if current_user.role != "admin":
        return {"error": "Unauthorized access"}
    
    new_ceremony = Ceremony(
        title=ceremony.title,
        text=ceremony.text,
        date=ceremony.date
    )
    db.add(new_ceremony)
    db.commit()
    return {"message": "Ceremony created successfully", "id": new_ceremony.id}

def update_ceremony(ident: int, ceremony: Ceremony_update, current_user, db):
    if current_user.role != "admin":
        return {"error": "Unauthorized access"}
    
    existing_ceremony = db.query(Ceremony).filter(Ceremony.id == ident).first()
    if not existing_ceremony:
        return {"error": "Ceremony not found"}
    
    existing_ceremony.title = ceremony.title
    existing_ceremony.text = ceremony.text
    existing_ceremony.date = ceremony.date
    
    db.commit()
    return {"message": "Ceremony updated successfully"}

def delete_ceremony(ident: int, current_user, db):
    if current_user.role != "admin":
        return {"error": "Unauthorized access"}
    
    ceremony = db.query(Ceremony).filter(Ceremony.id == ident).first()
    if not ceremony:
        return {"error": "Ceremony not found"}
    
    db.delete(ceremony)
    db.commit()
    return {"message": "Ceremony deleted successfully"}