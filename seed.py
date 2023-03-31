from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from classes.base import Base
from classes.custom_team import Custom_Team
from classes.Managers import Managers
from classes.Players import Players

engine = create_engine('sqlite:///nba.db')

Base.metadata.create_all(engine)
with Session(engine) as session:

    # Jonah = Players(name="Jonah", Team="Lakers", Position="Center", Outside_Scoring=80,
    #                 Inside_scoring=75, Defending=77, Athleticism=65, Playmaking=87, Rebounding=81, Cost=500)
    # Maile = Players(name="Maile", Team="Celtics", Position="Point Guard", Outside_Scoring=80,
    #                 Inside_scoring=75, Defending=77, Athleticism=65, Playmaking=87, Rebounding=81, Cost=750)
    # jake = Players(name="jake", Team="Hawks", Position="Shooting Guard", Outside_Scoring=80,
    #                Inside_scoring=75, Defending=77, Athleticism=65, Playmaking=87, Rebounding=81, Cost=750)
    # Ryan = Players(name="Ryan", Team="Nuggets", Position="Power Forward", Outside_Scoring=80,
    #                Inside_scoring=75, Defending=77, Athleticism=65, Playmaking=87, Rebounding=81, Cost=750)
    # Max = Players(name="Max", Team="Clippers", Position="Small Forward", Outside_Scoring=80,
    #               Inside_scoring=75, Defending=77, Athleticism=65, Playmaking=87, Rebounding=81, Cost=750)

    # actual Players
    # point guards
    Luka_Doncic = Players(name="Luka Doncic", Team="Mavericks", Position="Point Guard", Outside_Scoring=93,
                          Inside_scoring=85, Defending=70, Athleticism=86, Playmaking=95, Rebounding=78, Cost=1200)
    Ja_Morant = Players(name="Ja Morant", Team="Grizzlies", Position="Point Guard", Outside_Scoring=89,
                        Inside_scoring=72, Defending=69, Athleticism=88, Playmaking=95, Rebounding=54, Cost=900)
    James_Harden = Players(name="James Harden", Team="Sixers", Position="Point Guard", Outside_Scoring=87,
                           Inside_scoring=76, Defending=64, Athleticism=89, Playmaking=90, Rebounding=53, Cost=750)
    Damian_Lillard = Players(name="Damian Lillard", Team="Trailblazers", Position="Point Guard", Outside_Scoring=95,
                             Inside_scoring=64, Defending=61, Athleticism=88, Playmaking=89, Rebounding=46, Cost=600)
    Steph_Curry = Players(name="Steph Curry", Team="Warriors", Position="Point Guard", Outside_Scoring=96,
                          Inside_scoring=59, Defending=63, Athleticism=82, Playmaking=89, Rebounding=52, Cost=600)
    Tyrese_Haliburton = Players(name="Tyrese Haliburton", Team="Pacers", Position="Point Guard", Outside_Scoring=91,
                                Inside_scoring=64, Defending=68, Athleticism=80, Playmaking=93, Rebounding=43, Cost=600)
    Kyrie_Irving = Players(name="Kyrie Irving", Team="Mavericks", Position="Point Guard", Outside_Scoring=93,
                           Inside_scoring=63, Defending=63, Athleticism=79, Playmaking=88, Rebounding=48, Cost=500)
    Trae_Young = Players(name="Trae Young", Team="Hawks", Position="Point Guard", Outside_Scoring=89,
                         Inside_scoring=55, Defending=49, Athleticism=79, Playmaking=88, Rebounding=40, Cost=900)
    # # Small Forwards
    Lebron_James = Players(name="Lebron James", Team="Lakers", Position="Small Forward", Outside_Scoring=87,
                           Inside_scoring=91, Defending=82, Athleticism=92, Playmaking=88, Rebounding=76, Cost=1200)
    Jimmy_Butler = Players(name="Jimmy Butler", Team="Heat", Position="Small Forward", Outside_Scoring=87,
                           Inside_scoring=81, Defending=85, Athleticism=85, Playmaking=83, Rebounding=63, Cost=1000)
    Kawhi_Leonard = Players(name="Kawhi Leonard", Team="Clippers", Position="Small Forward", Outside_Scoring=91,
                            Inside_scoring=79, Defending=86, Athleticism=83, Playmaking=79, Rebounding=56, Cost=900)
    Jaylen_Brown = Players(name="Jaylen Brown", Team="Celtics", Position="Small Forward", Outside_Scoring=91,
                           Inside_scoring=78, Defending=78, Athleticism=83, Playmaking=77, Rebounding=55, Cost=750)
    Zach_Lavine = Players(name="Zach Lavine", Team="Bulls", Position="Small Forward", Outside_Scoring=89,
                          Inside_scoring=75, Defending=61, Athleticism=83, Playmaking=80, Rebounding=45, Cost=500)
    # # Power Forwards
    Giannis_AntetoKounmpo = Players(name="Giannis AntetoKounmpo", Team="Bucks", Position="Power Forward", Outside_Scoring=83,
                                    Inside_scoring=88, Defending=85, Athleticism=91, Playmaking=85, Rebounding=77, Cost=1200)
    Jayson_Tatum = Players(name="Jayson Tatum", Team="Celtics", Position="Power Forward", Outside_Scoring=92,
                           Inside_scoring=84, Defending=84, Athleticism=84, Playmaking=79, Rebounding=78, Cost=1200)
    Kevin_Durant = Players(name="Kevin Durant", Team="Suns", Position="Power Forward", Outside_Scoring=95,
                           Inside_scoring=85, Defending=77, Athleticism=81, Playmaking=82, Rebounding=59, Cost=1000)
    Pascal_Siakam = Players(name="Pascal Siakam", Team="Raptors", Position="Power Forward", Outside_Scoring=85,
                            Inside_scoring=87, Defending=73, Athleticism=80, Playmaking=74, Rebounding=63, Cost=900)
    Zion_Williamson = Players(name="Zion Williamson", Team="Pelicans", Position="Power Forward", Outside_Scoring=85,
                              Inside_scoring=93, Defending=58, Athleticism=86, Playmaking=72, Rebounding=63, Cost=900)
    # Centers
    Joel_Embiid = Players(name="Joel Embiid", Team="Sixers", Position="Center", Outside_Scoring=93,
                          Inside_scoring=92, Defending=77, Athleticism=80, Playmaking=68, Rebounding=80, Cost=1200)
    Anthony_Davis = Players(name="Anthony Davis", Team="Lakers", Position="Center", Outside_Scoring=84,
                            Inside_scoring=88, Defending=82, Athleticism=87, Playmaking=64, Rebounding=85, Cost=1000)
    Nikola_Jokic = Players(name="Nikola Jokic", Team="Nuggets", Position="Center", Outside_Scoring=93,
                           Inside_scoring=90, Defending=57, Athleticism=77, Playmaking=84, Rebounding=81, Cost=1000)
    Bam_Adebayo = Players(name="Bam Adebayo", Team="Heat", Position="Center", Outside_Scoring=75,
                          Inside_scoring=81, Defending=78, Athleticism=84, Playmaking=69, Rebounding=74, Cost=900)
    Domantas_Sabonis = Players(name="Domantas Sabonis", Team="Kings", Position="Center", Outside_Scoring=89,
                               Inside_scoring=84, Defending=54, Athleticism=72, Playmaking=68, Rebounding=83, Cost=600)
    Karl_Anthony_Towns = Players(name="Karl-Anthony Towns", Team="Timberwolves", Position="Center", Outside_Scoring=88,
                                 Inside_scoring=83, Defending=58, Athleticism=81, Playmaking=68, Rebounding=66, Cost=500)
    # Shooting Guards

    Shai_Gilgeous_Alexander = Players(name="Shai Gilgeous-Alexander", Team="Thunder", Position="Shooting Guard", Outside_Scoring=93,
                                      Inside_scoring=77, Defending=76, Athleticism=84, Playmaking=92, Rebounding=57, Cost=1000)
    Donovan_Mitchell = Players(name="Donovan Mitchell", Team="Cavaliers", Position="Shooting Guard", Outside_Scoring=92,
                               Inside_scoring=70, Defending=72, Athleticism=88, Playmaking=85, Rebounding=46, Cost=750)
    Paul_George = Players(name="Paul George", Team="Clippers", Position="Shooting Guard", Outside_Scoring=89,
                               Inside_scoring=69, Defending=80, Athleticism=83, Playmaking=78, Rebounding=53, Cost=750)
    Devin_Booker = Players(name="Devin Booker", Team="Suns", Position="Shooting Guard", Outside_Scoring=93,
                           Inside_scoring=76, Defending=61, Athleticism=79, Playmaking=85, Rebounding=46, Cost=600)
    DeMar_Derozan = Players(name="DeMar Derozan", Team="Bulls", Position="Shooting Guard", Outside_Scoring=92,
                            Inside_scoring=81, Defending=65, Athleticism=86, Playmaking=76, Rebounding=45, Cost=500)
    David_Doan = Players(name="David Tab Master Doan", Team="Flatiron", Position="Shooting Guard", Outside_Scoring=50,
                         Inside_scoring=50, Defending=50, Athleticism=50, Playmaking=50, Rebounding=50, Cost=0)
    Sam_Waters = Players(name="Sam 8 Mile Waters ", Team="Flatiron", Position="Shooting Guard", Outside_Scoring=50,
                         Inside_scoring=50, Defending=50, Athleticism=50, Playmaking=50, Rebounding=50, Cost=0)

    MrPeck = Managers(name="Mr. Peck", hometown="Los Angeles", budget=3000)
    MrsPeck = Managers(name="Mrs. Peck", hometown="Phoenix", budget=1500)

    Jonah_Team = Custom_Team(manager_id=1, budget=1500, Point_Guard_id=2,
                             Shooting_Guard_id=3, Small_Forward_id=4, Power_Forward_id=5, Center_id=1)
    Maile_Team = Custom_Team(manager_id=2, budget=3000, Point_Guard_id=2,
                             Shooting_Guard_id=3, Small_Forward_id=4, Power_Forward_id=5, Center_id=1)

    everything = [Luka_Doncic, Ja_Morant, James_Harden, Damian_Lillard, Steph_Curry, Tyrese_Haliburton, Kyrie_Irving, Trae_Young, Lebron_James,
                  Jimmy_Butler, Kawhi_Leonard, Jaylen_Brown, Zach_Lavine, Giannis_AntetoKounmpo, Jayson_Tatum, Kevin_Durant, Pascal_Siakam, Zion_Williamson,
                  Joel_Embiid, Anthony_Davis, Nikola_Jokic, Bam_Adebayo, Domantas_Sabonis, Karl_Anthony_Towns, Shai_Gilgeous_Alexander,
                  Donovan_Mitchell, Paul_George, Devin_Booker, DeMar_Derozan, David_Doan, Sam_Waters,

                  Jonah_Team, Maile_Team, MrPeck, MrsPeck]
    session.add_all(everything)
    session.commit()
