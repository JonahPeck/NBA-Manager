from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from classes.base import Base
from classes.custom_team import Custom_Team
from classes.Managers import Managers
from classes.Players import Players

engine = create_engine('sqlite:///nba.db')

Base.metadata.create_all(engine)
with Session(engine) as session:

    Jonah = Players(name="Jonah", Team="Lakers", Position="Center", Outside_Scoring=80,
                    Inside_scoring=75, Defending=77, Athleticism=65, Playmaking=87, Rebounding=81, Cost=500)
    Maile = Players(name="Maile", Team="Celtics", Position="Point Guard", Outside_Scoring=80,
                    Inside_scoring=75, Defending=77, Athleticism=65, Playmaking=87, Rebounding=81, Cost=750)
    jake = Players(name="jake", Team="Hawks", Position="Shooting Guard", Outside_Scoring=80,
                   Inside_scoring=75, Defending=77, Athleticism=65, Playmaking=87, Rebounding=81, Cost=750)
    Ryan = Players(name="Ryan", Team="Nuggets", Position="Power Forward", Outside_Scoring=80,
                   Inside_scoring=75, Defending=77, Athleticism=65, Playmaking=87, Rebounding=81, Cost=750)
    Max = Players(name="Max", Team="Clippers", Position="Small Forward", Outside_Scoring=80,
                  Inside_scoring=75, Defending=77, Athleticism=65, Playmaking=87, Rebounding=81, Cost=750)

    # actual Players
    # Luka_Doncic = Players(name="Luka Doncic", Team="Mavericks", Position="Point Guard", Outside_Scoring=93,
    #                       Inside_scoring=85, Defending=70, Athleticism=86, Playmaking=95, Rebounding=78, Cost=1200)
    # Ja_Morant = Players(name="Ja Morant", Team="Grizzlies", Position="Point Guard", Outside_Scoring=89,
    #                     Inside_scoring=72, Defending=69, Athleticism=88, Playmaking=95, Rebounding=54, Cost=900)
    # James_Harden = Players(name="James Harden", Team="Sixers", Position="Point Guard", Outside_Scoring=87,
    #                        Inside_scoring=76, Defending=64, Athleticism=89, Playmaking=90, Rebounding=53, Cost=750)
    # Damian_Lillard = Players(name="Damian Lillard", Team="Trailblazers", Position="Point Guard", Outside_Scoring=95,
    #                          Inside_scoring=64, Defending=61, Athleticism=88, Playmaking=89, Rebounding=46, Cost=600)
    # Steph_Curry = Players(name="Steph Curry", Team="Warriors", Position="Point Guard", Outside_Scoring=96,
    #                       Inside_scoring=59, Defending=63, Athleticism=82, Playmaking=89, Rebounding=52, Cost=600)
    # Ja_Morant = Players(name="Ja Morant", Team="Grizzlies", Position="Point Guard", Outside_Scoring=89,
    #                     Inside_scoring=72, Defending=69, Athleticism=88, Playmaking=95, Rebounding=54, Cost=900)
    # Ja_Morant = Players(name="Ja Morant", Team="Grizzlies", Position="Point Guard", Outside_Scoring=89,
    #                     Inside_scoring=72, Defending=69, Athleticism=88, Playmaking=95, Rebounding=54, Cost=900)
    # Ja_Morant = Players(name="Ja Morant", Team="Grizzlies", Position="Point Guard", Outside_Scoring=89,
    #                     Inside_scoring=72, Defending=69, Athleticism=88, Playmaking=95, Rebounding=54, Cost=900)

    MrPeck = Managers(name="Mr. Peck", hometown="Los Angeles", budget=3000)
    MrsPeck = Managers(name="Mrs. Peck", hometown="Phoenix", budget=1500)

    Jonah_Team = Custom_Team(manager_id=1, budget=1500, Point_Guard_id=2,
                             Shooting_Guard_id=3, Small_Forward_id=4, Power_Forward_id=5, Center_id=1)
    Maile_Team = Custom_Team(manager_id=2, budget=3000, Point_Guard_id=2,
                             Shooting_Guard_id=3, Small_Forward_id=4, Power_Forward_id=5, Center_id=1)

    everything = [Jonah, Maile, jake, Ryan, Max,
                  Jonah_Team, Maile_Team, MrPeck, MrsPeck]
    session.add_all(everything)
    session.commit()
