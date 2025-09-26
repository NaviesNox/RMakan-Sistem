
from fastapi import FastAPI
from app.api.v1.meja import meja_routes
from app.api.v1.users import users_routes
from app.api.v1.reservation import reservation_routes
from app.api.v1.payment import payment_routes
from app.api.v1.feedback import feedback_routes
from app.api.v1.auth import auth_routes

app = FastAPI(
    title="Restaurant Reservation API",
    version="1.0.0",
    description="API untuk sistem reservasi restoran",
)



""" Register routers dengan prefix dan tags """

app.include_router(auth_routes.router)


app.include_router(meja_routes.router, prefix="/meja", tags=["Meja"])
app.include_router(users_routes.router, prefix="/user", tags=["User"])
app.include_router(reservation_routes.router, prefix="/reservation", tags=["Reservation"])
app.include_router(payment_routes.router, prefix="/payment", tags=["Payment"])
app.include_router(feedback_routes.router, prefix="/feedback", tags=["Feedback"])



"""Root endpoint"""
@app.get("/")
def read_root():
    return {"message": "Welcome to Restaurant Reservation API"}




