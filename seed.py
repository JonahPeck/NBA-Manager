from sqlalchemy import *
from sqlalchemy.orm import *
from classes.base import Base
from classes.custom_team import Custom_Team
from classes.Managers import Managers
from classes.Players import Players

engine = create_engine('sqlite:///nba.db')

Base.metadata.create_all(engine)
with Session(engine) as session:

    Jonah = Players(name="Jonah", Team="Man U", Position="Center", Cost=5)
    Maile = Players(name="Maile", Team="Chelsea",
                    Position="Point Guard", Cost=25)
    Jonah_Team = Custom_Team(manager="Jonah", Point_Guard="Steph Curry",
                             Shooting_Guard="Michael Jordan", Small_Forward="Lebron", Power_Forward="Charles Barkley", Center="Shaq")
    Maile_Team = Custom_Team(manager="Maile", Point_Guard="Steph Curry",
                             Shooting_Guard="Michael Jordan", Small_Forward="Lebron", Power_Forward="Charles Barkley", Center="Shaq")
    MrPeck = Managers(name="Mr. Peck", hometown="Los Angeles", budget=3000)
    MrsPeck = Managers(name="Mrs. Peck", hometown="Phoenix", budget=1500)

    everything = [Jonah, Maile, Jonah_Team, Maile_Team, MrPeck, MrsPeck]
    session.add_all(everything)
    session.commit()
