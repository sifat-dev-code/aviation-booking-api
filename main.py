from fastapi import FastAPI 
from database import SessionLocal, engine, Base
from routes import flights
import models
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(flights.router)


