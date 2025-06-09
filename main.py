from fastapi import FastAPI
from router.login import login_router
from router.users import users_router
from router.news import news_router
from router.documents import documents_router
from router.reg_manag import reg_manag_router
from router.manag import manag_router
from router.ceremony import ceremony_router
from router.tenders import tenders_router 
from router.events import events_router
from db import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(documents_router)
app.include_router(news_router)
app.include_router(events_router)
app.include_router(reg_manag_router)
app.include_router(manag_router)
app.include_router(ceremony_router)
app.include_router(tenders_router)

app.include_router(login_router)