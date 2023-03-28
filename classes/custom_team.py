from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, validates
from .base import Base


class Custom_Team(Base):
    __tablename__ = "Custom Team"
    id = Column(Integer(), primary_key=True)
    manager = Column(String())
    budget = Column(String())
    Point_Guard = Column(String())
    Shooting_Guard = Column(String())
    Small_Forward = Column(String())
    Power_Forward = Column(String())
    Center = Column(String())
    players_id = Column(Integer(), ForeignKey('Players.id'))
    managers_id = Column(Integer()), ForeignKey('Managers.id')
