from fastapi import FastAPI 
from database import SessionLocal, engine, Base
from routes import flights
from routes import bookings
from routes import users
import models
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(flights.router)
app.include_router(bookings.router)


app.include_router(users.router)