# Aviation Booking & Flight Management API

A production-ready RESTful API built with **FastAPI**, **SQLAlchemy ORM**, and **PostgreSQL** designed to handle core airline operations, flight scheduling, and inventory management.

## Key Features & Architecture
- **Modular Routing:** Structured using FastAPI's `APIRouter` for clean separation of concerns and scalability.
- **Database Persistence:** Relational data modeling and session management powered by **PostgreSQL** and **SQLAlchemy**.
- **Strict Data Validation:** Request and response payload validation enforced via **Pydantic** schemas.
- **Complete CRUD Operations:**
  - `POST /flights/` — Schedule and create new flight records.
  - `GET /flights/` — Retrieve real-time flight schedules and pricing.
  - `PUT /flights/{flight_id}` — Update flight routes, schedules, and base fares.
  - `DELETE /flights/{flight_id}` — Remove cancelled or obsolete flight entries.

## Tech Stack
- **Language:** Python 3.x
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Server:** Uvicorn (ASGI)

## Quick Start
1. Clone the repository:
   `git clone https://github.com/sifat-dev-code/aviation-booking-api.git`
2. Install dependencies:
   `pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic`
3. Run the development server:
   `uvicorn main:app --reload`
4. Access interactive API documentation (Swagger UI):
   `http://127.0.0.1:8000/docs`