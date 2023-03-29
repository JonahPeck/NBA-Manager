# import data from other databases
# start by
from clipaths.Hometown import hometown_selection
from clipaths.Roster import roster_selection
from classes.Players import Players
from classes.Managers import Managers
from classes.custom_team import Custom_Team
from classes.base import Base
from sqlalchemy.orm import *
from sqlalchemy import *


# playersdb = PlayersDB('database.db')
if __name__ == '__main__':
    engine = create_engine('sqlite:///nba.db')
    Base.metadata.create_all(engine)

    print('''


   o       |   __   |
      \_ O |  |__|  |
   ____/ \ |___WW___|
   __/   /     ||
               ||
               ||
_______________||________________

WELCOME TO NBA MANAGER

_________________________________


    ''')
    with Session(engine) as session:
        start_game = True
        get_manager_names = True
        while start_game:
            Greeting = input("Are you ready to play? (yes or no)")
            if Greeting == "yes":
                start_game = False
            else:
                print("Okay...")
        manager1 = None
        while get_manager_names:
            manager1 = input("Manager #1 - What is your name?: ")
            if isinstance(manager1, str):
                get_manager_names = False
                print(f'Welcome to the game {manager1}!')
                manager1 == manager1
            else:
                print("C'mon give me a real name")
            manager2 = None
            manager2 = input("Manager #2 - What is your name?: ")
            if isinstance(manager2, str):
                manager2 == manager2
                print(f'Welcome to the game {manager2}!')
            else:
                print("C'mon give me a real name")

        print(f"Today's matchup will be {manager1} vs {manager2}!!!")
        # userinput
    print('''
             -|
               -' |
             -'   | __().
        ==wkm=====|'\/   `.O__
                            \ `,
                           _-^.
                           `.  `---,
                             :



       ____________________________________
       ///\\\///\\\///\\\///\\\///\\\///\\\
    ''')
hometown_selection(session, manager1, manager2)
roster_selection(session, manager1, manager2)
# print(
# f'{manager1} what is your hometown? Please select from the list below: ')
