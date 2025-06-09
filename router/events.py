from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database
from model.events import Event
from schema.events import Event_create, Event_update
from router.login import get_current_user
from model.users import Users
from func.events import show_event, create_event, update_event, delete_event

events_router = APIRouter(tags=["events"])

@events_router.get("/events_get")
def get_event(event_id: int = None, db: Session = Depends(database)):
    return show_event(event_id, db)

@events_router.post("/events_create")
def create_new_event(event: Event_create, current_user: Users=Depends(get_current_user), db: Session = Depends(database)):
    return create_event(event, current_user, db)

@events_router.put("/events_update/")
def update_existing_event(event_id: int, event: Event_update, current_user: Users=Depends(get_current_user), db: Session = Depends(database)):
    return update_event(event_id, event, current_user, db)

@events_router.delete("/events_delete/")
def delete_existing_event(event_id: int, current_user: Users=Depends(get_current_user), db: Session = Depends(database)):
    return delete_event(event_id, current_user, db)