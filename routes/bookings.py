from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import get_db

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

class BookingCreate(BaseModel):
    flight_id: int
    passenger_id: int

@router.post("/")
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    
    flight = db.query(models.Flight).filter(models.Flight.id == booking.flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    
    
    passenger = db.query(models.Passenger).filter(models.Passenger.id == booking.passenger_id).first()
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")

    
    new_booking = models.Booking(
        flight_id=booking.flight_id,
        passenger_id=booking.passenger_id
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return {"message": "Ticket Booked Successfully!", "data": new_booking}
@router.get("/")
def get_all_bookings(db: Session = Depends(get_db)):
    ticket = db.query(models.Booking).all()
    return ticket