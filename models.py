from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import ENUM
from app.core.database import Base
from app.model.v1.meja.meja_schemas import LocationEnum, StatusEnum

Base = declarative_base()
metadata = Base.metadata
# Definisikan ENUM global sekali
role_enum = ENUM(
    'admin', 'waiter', 'manager', 'reservationStaff', 'customer',
    name='roleenum', create_type=True, metadata=Base.metadata
)

payment_method_enum = ENUM(
    'cash', 'card', 'e_wallet',
    name='paymentmethodenum', create_type=True, metadata=Base.metadata
)

payment_status_enum = ENUM(
    'pending', 'completed', 'failed',
    name='paymentstatusenum', create_type=True, metadata=Base.metadata
)

reservation_status_enum = ENUM(
    'pending', 'confirmed', 'cancelled',
    name='reservationstatusenum', create_type=True, metadata=Base.metadata
)


"""Model ORM dan schema untuk Feedback """
class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    id_users= Column(Integer, ForeignKey("users.id"), nullable=False)
    id_reservation = Column(Integer, ForeignKey("reservation.id"), nullable=False)  
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    # Relations
    user        = relationship("Users", back_populates="feedbacks")
    reservation = relationship("Reservation", back_populates="feedback") 


"""Model ORM dan schema untuk Meja """
class Meja(Base):
    __tablename__ = "meja"

    id = Column(Integer, primary_key=True, index=True)
    table_number = Column(Integer, unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)
    location = Column(ENUM(LocationEnum, name="location_enum", create_type=True, ), nullable=False)
    status = Column(ENUM(StatusEnum, name="status_enum", create_type=True,), nullable=False)

    # Relationship
    reservations = relationship("Reservation", back_populates="meja")


"""Model ORM dan schema untuk Payment """
class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_reservation = Column(Integer, ForeignKey("reservation.id"), nullable=False) 
    amount = Column(Float, nullable=False)
    method = Column(payment_method_enum, nullable=False)
    status = Column(payment_status_enum, nullable=False)
    transaction_time = Column(DateTime, nullable=False)

    # Relationships
    reservations = relationship("Reservation", back_populates="payment")


"""Model ORM dan schema untuk Reservation """
class Reservation(Base):
    __tablename__ = "reservation"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
     
    id_meja = Column(Integer, ForeignKey("meja.id"), nullable=False)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    reservation_time = Column(DateTime, nullable=False)
    guest_count = Column(Integer, nullable=False)
    notes = Column(String, nullable=True)
    status = Column(reservation_status_enum,  nullable=False, default="pending" )
    id_staff = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Relationships
    meja = relationship("Meja", back_populates="reservations")
    payment = relationship("Payment", back_populates="reservations")
    customer = relationship(
        "Users",
        foreign_keys=[id_user],
        back_populates="reservations_as_customer"
    )
    staff = relationship(
        "Users",
        foreign_keys=[id_staff],
        back_populates="reservations_as_staff"
    )
    feedback = relationship("Feedback", back_populates="reservation", uselist=False)


"""Model ORM User """
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(role_enum, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String, nullable=False, unique=True)    
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    reservations_as_customer = relationship(
        "Reservation",
        foreign_keys="[Reservation.id_user]",
        back_populates="customer"
    )
    reservations_as_staff = relationship(
        "Reservation",
        foreign_keys="[Reservation.id_staff]",
        back_populates="staff"
    )
    feedbacks    = relationship("Feedback", back_populates="user")