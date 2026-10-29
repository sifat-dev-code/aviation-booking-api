from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True, index= True)
    name = Column (String, nullable= False)
    email= Column(String, unique= True,index=True, nullable=False)
    hashed_password= Column(String,  nullable= False)
    role = Column(String, default="Passenger")

class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key= True, index= True)
    flight_number= Column(String, unique= True,index=True, nullable= False)
    origin = Column(String, nullable=False)
    destination = Column(String,nullable=False)
    departure_time = Column(DateTime, nullable= False)
    arrival_time= Column(DateTime, nullable= False)
    base_price = Column(Float, nullable= False)
    passengers = relationship("Passenger", back_populates="flight")
class Seat (Base):
    __tablename__ = "seats"
    id = Column(Integer, primary_key= True, index= True)
    flight_id = Column(Integer, ForeignKey("flights.id"), nullable= False)
    seat_number = Column(String, nullable=False)
    class_type = Column (String, nullable= False)
    is_available= Column(Boolean, default= True)

class Passenger(Base):
    __tablename__ = "passengers"
    
    id = Column(Integer, primary_key= True, index= True)
    name = Column (String, nullable= False)
    email= Column(String, unique= True,index=True, nullable=False)
    flight_id = Column(Integer, ForeignKey("flights.id"), nullable= False)
    flight = relationship("Flight", back_populates="passengers")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    
    flight_id = Column(Integer, ForeignKey("flights.id"))
    passenger_id = Column(Integer, ForeignKey("passengers.id"))
    
    booking_date = Column(DateTime, default=datetime.now)
    status = Column(String, default="Confirmed")