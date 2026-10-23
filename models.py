from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
import datetime

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
class Seat (Base):
    __tablename__ = "seats"
    id = Column(Integer, primary_key= True, index= True)
    flight_id = Column(Integer, ForeignKey("flights.id"), nullable= False)
    seat_number = Column(String, nullable=False)
    class_type = Column (String, nullable= False)
    is_available= Column(Boolean, default= True)
class Booking(Base):
    __tablename__= "bookings"
    id = Column(Integer, primary_key= True, index= True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable= False)
    flight_id = Column (Integer, ForeignKey("flights.id"), nullable= False)
    seat_id = Column(Integer, ForeignKey("seats.id"), nullable= False)
    total_price = Column(Float, nullable= False)
    payment_status= Column (String, default= "Pending..")
    booking_time = Column(DateTime, default= datetime.datetime.utcnow)