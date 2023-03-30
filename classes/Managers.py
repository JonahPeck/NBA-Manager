from sqlalchemy import Column, String, Integer, create_engine, func
from sqlalchemy.orm import Session, relationship, validates
from .base import Base


class Managers(Base):
    __tablename__ = "Managers"
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    hometown = Column(String())
    budget = Column(Integer())

    def add_to_db(self, session):
        session.add(self)
        session.commit()

    @classmethod
    def get_manager(cls, session, manager):
        filtered_managers = session.query(Managers).filter(
            Managers.name == manager).first()
        return filtered_managers

        # def add_budget(self, session, hometown):
        #     from .custom_team import Custom_Team
        #     from .Players import Players
        #     new_budget = Managers()

        # def add_player(self,session,player_name):
        # from .player_table import Player
        # from .dnd_games import DndGame
        # filtered_player=session.query(Player).filter(Player.name==player_name).first()
        # dnd_class = input("What Class? ")
        # game_name = input("Name of Game? ")
        # newgame = DndGame(game_name = game_name,player_class=dnd_class,dm_id=self.id,player_id=filtered_player.id)
        # session.add(newgame)
        # session.commit()
        # print(self.players)
