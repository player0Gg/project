from model.news import News
from schema.news import News_create, News_update
from utils.save_files import save_file


def show_news(ident, db):
    if ident:
        news = db.query(News).filter(News.id == ident).first()
    else:
        news = db.query(News).all()
        return news
    

def create_news(news: News_create, current_user, db):
    if current_user.role != "admin":
        return {"error": "You are not admin"}
    else:
        news = News(
            create_at=news.create_at,
            title=news.title,
            description=news.description,
            text=news.text
        )
        db.add(news)
        db.commit()
        
        return {"message": "News created successfully"}
    

def update_news(ident, news: News_update, current_user, db):
    if current_user.role != "admin":
        return {"error": "You are not admin"}
    
    
    if not db.query(News).filter(News.id == ident).first():
        return {"error": "News not found"}
    else:
        db.query(News).filter(News.id == ident).update({
            News.create_at: news.create_at,
            News.title: news.title,
            News.description: news.description,
            News.text: news.text
        })

    db.commit()
    return {"message": "News updated successfully"}


def delete_news(news_id, current_user, db):
    if current_user.role != "admin":
        return {"error": "You are not admin"}
    
    news_to_delete = db.query(News).filter(News.id == news_id).first()
    if not news_to_delete:
        return {"error": "News not found"}
    
    db.delete(news_to_delete)
    db.commit()
    return {"message": "News deleted successfully"}