# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base
from .base import Base
# Base = declarative_base()


class Players(Base):
    __tablename__ = "Players"

    id = Column(Integer(), primary_key=True)
    # manager = Column(String())
    name = Column(String())
    Team = Column(String())
    Position = Column(String())
    Cost = Column(Integer())
    Outside_Scoring = Column(Integer())
    Inside_scoring = Column(Integer())
    Defending = Column(Integer())
    Athleticism = Column(Integer())
    Playmaking = Column(Integer())
    Rebounding = Column(Integer())

    @classmethod
    def filter_by(cls, session):
        filtered_players = session.query(Players).filter(Players.name == input)
        # query by cls
        # access the object and from there access the cost and sum up the attributes

        # if __name__ == '__main__':

        #     engine = create_engine('sqlite:///nba.db')

        #     with Session(engine) as session:
        #         BillyBob = Players(name="Billy Bob",
        #                            Team="Flatiron",
        #                            Position="Point Guard",
        #                            Cost=1200,
        #                            Outside_Scoring=80,
        #                            Inside_Scoring=80,
        #                            Athleticism=80,
        #                            Playmanking=80,
        #                            Rebounding=80)
        #         JimBob = Players(name="Jim Bob",
        #                          Team="Flatiron JV",
        #                          Position="Center",
        #                          Cost=1500,
        #                          Outside_Scoring=85,
        #                          Inside_Scoring=85,
        #                          Athleticism=85,
        #                          Playmanking=85,
        #                          Rebounding=85)

        #         session.add(BillyBob)
        #         session.add(JimBob)
        #         session.commit()
