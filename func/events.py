from model.events import Event
from schema.events import Event_create, Event_update

def show_event(event_id: int, db):
    if event_id is None:
        return db.query(Event).all()
    else:
        return db.query(Event).filter(Event.id == event_id).first()
    
def create_event(event: Event_create, current_user,  db):
    if current_user.role != "admin":
        return {"error": "User not admin"}
    else:
        new_event = Event(
            title=event.title,
            text=event.text,
            date=event.date
        )
        db.add(new_event)
        db.commit()
        return {"message": "Event created successfully"}
    
def update_event(event_id: int, event: Event_update, current_user, db):
    if current_user.role != "admin":
        return {"error": "User not admin"}
    else:
        if not db.query(Event).filter(Event.id == event_id).first():
            return {"error": "Event not found"}
        else:
            db.query(Event).filter(Event.id == event_id).update({
                Event.title: event.title,
                Event.text: event.text,
                Event.date: event.date
            })
        
            db.commit()
            return {"message": "Event updated successfully"}
    
def delete_event(event_id: int, current_user, db):
    if current_user.role != "admin":
        return {"error": "User not admin"}
    else:
        existing_event = db.query(Event).filter(Event.id == event_id).first()
        if not existing_event:
            return {"error": "Event not found"}
        
        db.delete(existing_event)
        db.commit()
        return {"message": "Event deleted successfully"}
