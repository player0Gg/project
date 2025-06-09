from model.documents import Documents
from schema.documents import Documents_create, Documents_update

def get_documents(ident, db):
    doc_given = db.query(Documents).filter(Documents.id == ident).first()
    if doc_given:
        return doc_given
    else:
        return db.query(Documents).all()
    
def create_documents(documents:Documents_create ,current_user, db):
    if current_user.role!='admin':
        return {"message":"You are not an admin"}
    else:
        new_document=Documents(
            doc_date=documents.doc_date,
            title=documents.title,
            text=documents.text
        )
        db.add(new_document)
        db.commit()
        return {"message":"New document created successfully"}

def update_documents(ident:int, documents:Documents_update, current_user,db):
    if current_user.role!="admin":
        return {'message':"You are not admin"}
    
    if not db.query(Documents).filter(Documents.id == ident).first():
        return {"error": "Documents not found"}
    else:
        db.query(Documents).filter(Documents.id == ident).update({
            Documents.doc_date:documents.doc_date,
            Documents.title:documents.title,
            Documents.text:documents.text
        })
    db.commit()
    return {"message": "Documents updated successfully"}

def remove_documents(ident:int, current_user, db):
    if current_user.role!='admin':
        return {'message':"You are not an admin"}
    else:
        db.query(Documents).filter(Documents.id==ident).delete()
        db.commit()
        return {'message':"Document deleted successful"}
