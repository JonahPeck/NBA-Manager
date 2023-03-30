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
        return filtered_players

    @classmethod
    def get_player_figures(cls, session, player):
        filtered_players = session.query(Players).filter(
            Players.name == player).first()
        return filtered_players
