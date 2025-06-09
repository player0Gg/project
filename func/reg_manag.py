from model.reg_manag import Reg_manag

def show_regmanag(ident:int, db):
    if not ident:
        return db.query(Reg_manag).all()
    else:
        return db.query(Reg_manag).filter(Reg_manag.id == ident).first()
    
def add_regmanag(reg_manag, current_user, db):
    if current_user.role!='admin':
        return {'message':"You are not admin"}
    else:
        new_regmanag=Reg_manag(
            title=reg_manag.title,
            text=reg_manag.text,
            full_name=reg_manag.full_name,
            phone=reg_manag.phone,
            address=reg_manag.address
        )
        db.add(new_regmanag)
        db.commit()
        return {'message':"Added seccessful"}

def remake_regmanag(ident, reg_manag, current_user, db):
    if current_user.role!="admin":
        return {'message':"You are not admin"}
    else:
        if db.query(Reg_manag).filter(Reg_manag.id==ident).first():
            db.query(Reg_manag).filter(Reg_manag.id==ident).update({
                Reg_manag.title:reg_manag.title,
                Reg_manag.text:reg_manag.text,
                Reg_manag.full_name:reg_manag.full_name,
                Reg_manag.phone:reg_manag.phone,
                Reg_manag.address:reg_manag.address
            })
            db.commit()
            return {'message':"Remake does seccessful"}

def remove_regmanag(ident, current_user, db):
    if current_user.role!="admin":
        return {'message':"You are not admin"}
    else:
        db.query(Reg_manag).filter(Reg_manag.id==ident).delete()
        db.commit()
        return {'message':"Saccessfully delete"}