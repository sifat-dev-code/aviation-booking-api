from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from database import get_db
import models
router = APIRouter(
    prefix="/flights",
    tags=["Flights"]
)
class FlightCreate(BaseModel):
    flight_number: str
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    base_price: float

@router.post("/")
def create_flights(flight:FlightCreate, db:Session= Depends(get_db) ):
    new_flight = models.Flight(
    flight_number=flight.flight_number,
    origin = flight.origin,
    destination = flight.destination,
    departure_time = flight.departure_time,
    arrival_time = flight.arrival_time,
    base_price = flight.base_price
    )
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    return {"message": "Flight Created Successfully!", "data": new_flight}

@router.get("/")
def get_flights(db: Session = Depends(get_db)):
    flights = db.query(models.Flight).all()
    return {"status": "success", "data": flights}
