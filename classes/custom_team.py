from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, validates
from .base import Base


class Custom_Team(Base):
    __tablename__ = "Custom Team"
    id = Column(Integer(), primary_key=True)
    manager_id = Column(String(), ForeignKey('Managers.id'))
    budget = Column(String())
    Point_Guard_id = Column(String(), ForeignKey('Players.id'))
    Shooting_Guard_id = Column(String(), ForeignKey('Players.id'))
    Small_Forward_id = Column(String(), ForeignKey('Players.id'))
    Power_Forward_id = Column(String(), ForeignKey('Players.id'))
    Center_id = Column(String(), ForeignKey('Players.id'))
    # players_id = Column(Integer(), ForeignKey('Players.id'))
    # managers_id = Column(Integer()), ForeignKey('Managers.id')
