from sqlalchemy import Column, String, Integer, create_engine, func
from sqlalchemy.orm import Session, relationship, validates
from .base import Base


class Managers(Base):
    __tablename__ = "Managers"
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    hometown = Column(String())
    budget = Column(Integer())
