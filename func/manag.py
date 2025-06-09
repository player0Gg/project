from model.manag import Manag

def get_manag(ident: int, db):
    if not ident:
        return db.query(Manag).all()
    else:
        return db.query(Manag).filter(Manag.id == ident).first()
    
def create_manag(manag, current_user, db):
    if current_user.role != "admin":
        return {"error": "You are not admin."}
    else:
        new_manag = Manag(
            full_name=manag.full_name,
            phone_number=manag.phone_number,
            position=manag.position,
            free_day=manag.free_day,
            about=manag.about,
            author=manag.author
        )
        db.add(new_manag)
        db.commit()
        return {"message": "Management member created successfully."}
    
def update_manag(ident: int, manag, current_user, db):
    if current_user.role != "admin":
        return {"error": "You are not admin."}
    else:
        if db.query(Manag).filter(Manag.id == ident).first() is None:
            return {"error": "Management member not found."}
        else:
            db.query(Manag).filter(Manag.id == ident).update({
                Manag.full_name: manag.full_name,
                Manag.phone_number: manag.phone_number,
                Manag.position: manag.position,
                Manag.free_day: manag.free_day,
                Manag.about: manag.about,
                Manag.author: manag.author
            })
            db.commit()
            return {"message": "Management member updated successfully."}
    
def delete_manag(ident: int, current_user, db):
    if current_user.role != "admin":
        return {"error": "You are not admin."}
    else:
        if db.query(Manag).filter(Manag.id == ident).first() is None:
            return {"error": "Management member not found."}
        else:
            db.query(Manag).filter(Manag.id == ident).delete()
            db.commit()
            return {"message": "Management member deleted successfully."}
