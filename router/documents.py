from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from db import database
from model.documents import Documents
from model.users import Users
from schema.documents import Documents_create, Documents_update
from utils.save_files import save_file
from router.login import get_current_user
from func.documents import get_documents, create_documents, update_documents, remove_documents

documents_router = APIRouter(tags=["documents"])

@documents_router.get("/documents_get")
def documents_get(ident:int=None, db: Session=Depends(database)):
    return get_documents(ident,db)

@documents_router.post("/documents_post")
def documents_create(document:Documents_create, current_user:Users=Depends(get_current_user), db:Session=Depends(database)):
    return create_documents(document,current_user,db)

@documents_router.put("/document_update")
def document_update(ident:int, document:Documents_update, current_user:Users=Depends(get_current_user), db:Session=Depends(database)):
    return update_documents(ident,document,current_user,db)

@documents_router.put("/documents_save_files")
def documents_save_files(ident:int, file: UploadFile, current_user: Users=Depends(get_current_user), db: Session=Depends(database)):
    if current_user.role != "admin":
        return {"error": "You are not admin"}
    else:
        if not file.filename.endswith(('.pdf', '.docx', '.txt')):
            return {"error": "Invalid file type. Only PDF, DOCX, and TXT files are allowed."}
        else:
            file_path=save_file(file)
            documents=db.query(Documents).filter(Documents.id == ident).first()
            if not file_path:
                return {"error": "File saving failed"}
            else:
                documents.files_doc=file_path
    db.commit()
    return {"message": "File saved successfully"}

@documents_router.delete("/document_delete")
def delete_documents(ident:int, current_user:Users=Depends(get_current_user), db:Session=Depends(database)):
    return remove_documents(ident,current_user,db)