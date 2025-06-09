from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from utils.save_files import save_file
from model.news import News
from schema.news import News_create, News_update
from db import database
from router.login import get_current_user
from model.users import Users
from func.news import show_news, create_news, update_news, delete_news

news_router = APIRouter(tags=["News"])

@news_router.get("/news_show")
def get_news(ident: int = None, db: Session = Depends(database)):
    return show_news(ident, db)

@news_router.post("/news_create")
def create_news_endpoint(news: News_create, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return create_news(news, current_user, db)

@news_router.put("/news_update")
def update_news_endpoint(news_id: int, news: News_update, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return update_news(news_id, news, current_user, db)

@news_router.put("/news_image")
def update_news_image(news_id: int, file: UploadFile, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    if current_user.role != "admin":
        return {"error": "You are not admin"}
    else:
        image_path = save_file(file)
        news = db.query(News).filter(News.id == news_id).first()
        if not news:
            return {"error": "News not found"}
    
    news.image = image_path
    db.commit()
    return {"message": "Image updated successfully"}

@news_router.delete("/news_delete")
def delete_news_endpoint(news_id: int, current_user: Users = Depends(get_current_user), db: Session = Depends(database)):
    return delete_news(news_id, current_user, db)