from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Enum as SqlEnum, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM
from app.core.database import Base
from app.model.v1.meja.meja_schemas import LocationEnum, StatusEnum



Base = declarative_base()
metadata = Base.metadata

"""Model ORM dan schema untuk Customer """
class Customer(Base):
    __tablename__ = "customer"

    id_customer = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    role = Column(String(20), nullable=False, server_default="customer")
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    reservations = relationship("Reservation", back_populates="customer")
    feedback = relationship("Feedback", back_populates="customer")


"""Model ORM dan schema untuk Feedback """
class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    id_customer = Column(Integer, ForeignKey("customer.id_customer"), nullable=False)
    id_reservation = Column(Integer, ForeignKey("reservation.id"), nullable=False)  
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    #Relations
    customer = relationship("Customer", back_populates="feedback")
    reservations = relationship("Reservation", back_populates="feedback")  



"""Model ORM dan schema untuk Meja """
class Meja(Base):
    __tablename__ = "meja"

    id = Column(Integer, primary_key=True, index=True)
    table_number = Column(Integer, unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)
    location = Column(SqlEnum(LocationEnum, name="location_enum"), nullable=False)
    status = Column(SqlEnum(StatusEnum, name="status_enum"), nullable=False)

    # Relationship
    reservations = relationship("Reservation", back_populates="meja")


"""Model ORM dan schema untuk Payment """
class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_reservation = Column(Integer, ForeignKey("reservation.id"), nullable=False) 
    amount = Column(Float, nullable=False)
    method = Column(
        ENUM('cash', 'card', 'e_wallet', name='paymentmethodenum', create_type=False),
        nullable=False
    )
    status = Column(
        ENUM('pending', 'completed', 'failed', name='paymentstatusenum', create_type=False),
        nullable=False
    )
    transaction_time = Column(DateTime, nullable=False)

    # Relationships
    reservations = relationship("Reservation", back_populates="payment")



"""Model ORM dan schema untuk Reservation """

class Reservation(Base):
    __tablename__ = "reservation"


    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_customer = Column(Integer, ForeignKey("customer.id_customer"), nullable=False)
    id_staff = Column(Integer, ForeignKey("staff.id"), nullable=True)  # bisa kosong dulu
    id_meja = Column(Integer, ForeignKey("meja.id"), nullable=False)
    reservation_time = Column(DateTime, nullable=False)
    guest_count = Column(Integer, nullable=False)
    notes = Column(String, nullable=True)
    status = Column(
        ENUM('pending', 'confirmed', 'cancelled', name='reservationstatusenum', create_type=False),
        nullable=False)
    
    # Relationships
    staff = relationship("Staff", back_populates="reservations")
    meja = relationship("Meja", back_populates="reservations")
    customer = relationship("Customer", back_populates="reservations")
    feedback = relationship("Feedback", back_populates="reservations", uselist=False)
    payment = relationship("Payment", back_populates="reservations")

"""Model ORM dan schema untuk Staff """
class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(
        ENUM('admin', 'waiter', 'manager', 'reservationStaff', name='roleenum', create_type=False),
        nullable=False
    )
    phone = Column(String, nullable=False, unique=True)    

    # Relationships
    reservations = relationship("Reservation", back_populates="staff")  


