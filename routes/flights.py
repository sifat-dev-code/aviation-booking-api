from fastapi import APIRouter, Depends, HTTPException, status
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
class PassengerCreate(BaseModel):
    name : str
    email : str
    flight_id : int 

class FlightResponse(BaseModel):
    id: int
    flight_number: str
    origin: str
    destination: str

    class Config:
        from_attributes = True  # Pydantic ke database model theke data nite bolche

class PassengerResponse(BaseModel):
    id: int
    name: str
    email: str
    flight: FlightResponse  # Etai magic! Flight er details ekhane nested hoye jabe

    class Config:
        from_attributes = True

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

@router.delete("/{flight_id}")
def delete_flight(flight_id: int, db: Session = Depends(get_db)):
    flight = db.query(models.Flight).filter(models.Flight.id == flight_id).first()
    if not flight:
        return {"error": "Flight not found!"}
    
    db.delete(flight)
    db.commit()
    return {"message": f"Flight {flight_id} deleted successfully!"}

@router.put("/{flight_id}")
def update_flight (flight_id: int,flight:FlightCreate,db: Session = Depends(get_db)):
    db_flight = db.query(models.Flight).filter(models.Flight.id == flight_id).first()
    if not db_flight:
        return {"error": "Flight not found"}
    db_flight.flight_number=flight.flight_number
    db_flight.origin = flight.origin
    db_flight.destination = flight.destination
    db_flight.departure_time = flight.departure_time
    db_flight.arrival_time = flight.arrival_time
    db_flight.base_price = flight.base_price
    db.commit()
    db.refresh(db_flight)
    return {"message": "Flight Updated Successfully!", "data": db_flight}

@router.post("/passengers/")
def create_passenger(passenger: PassengerCreate, db: Session = Depends(get_db)):
    new_passenger = models.Passenger(
        name = passenger.name,
        email = passenger.email,
        flight_id = passenger.flight_id
    )
    db.add(new_passenger)
    db.commit()
    db.refresh(new_passenger)
    return {"message": "Passenger booked successfully!", "data": new_passenger}
   
@router.get("/passengers/{passenger_id}",response_model = PassengerResponse)
def get_single_passenger(passenger_id: int, db: Session = Depends(get_db)):
    single_passengers = db.query(models.Passenger).filter(models.Passenger.id == passenger_id).first()
    if single_passengers is None:
        raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, detail= "Not found")
    return single_passengers

