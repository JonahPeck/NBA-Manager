# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base
from .base import Base
# Base = declarative_base()


class Players(Base):
    __tablename__ = "Players"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    Team = Column(String())
    Position = Column(String())
    Cost = Column(Integer())


if __name__ == '__main__':

    engine = create_engine('sqlite:///Players.db')

    with Session(engine) as session:
        BillyBob = Players(name="Billy Bob",
                           Team="Flatiron",
                           Position="Point Guard",
                           Cost=10)
        JimBob = Players(name="Jim Bob",
                         Team="Flatiron JV",
                         Position="Center",
                         Cost=15)

        session.add(BillyBob)
        session.add(JimBob)
        session.commit()
