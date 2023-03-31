from classes.Players import Players
from classes.Managers import Managers
from classes.custom_team import Custom_Team


def roster_selection(session, manager1, manager2, hometown_budget1, hometown_budget2):
    option1 = 0
    option2 = 0
    option3 = 0
    option4 = 0
    option5 = 0
    option6 = 0
    option7 = 0
    option8 = 0
    option9 = 0
    option10 = 0
    point_guard1 = 0
    point_guard2 = 0
    center1 = 0
    center2 = 0
    small_forward1 = 0
    small_forward2 = 0
    power_forward1 = 0
    power_forward2 = 0
    shooting_guard1 = 0
    shooting_guard2 = 0

    print("Let's build your rosters")
    print(f"{manager1.name}, choose a Point Guard")

    point_guard_list = ["Jonah", "Maile", "jake", "Ryan", "Max", "Luka Doncic", "Ja Morant", "James Harden", "Damian Lillard", "Steph Curry",
                        "Tyrese Haliburton", "Kyrie Irving", "Trae Young"]
    center_list = []
    dict_pg = {
        "Luka Doncic": 1200,
        "Ja Morant": 1000,
        "James Harden": 1000,
        "Damian Lillard": 900,
        "Steph Curry": 900,
        "Tyrese Haliburton": 750,
        "Kyrie Irving": 750,
        "Trae Young": 600,
        # "Jonah": 500,
        # "Maile": 750,
        # "jake": 750,
        # "Ryan": 750,
        # "Max": 750

    }
    dict_center = {
        "Joel Embiid": 1200,
        "Anthony Davis": 1000,
        "Nikola Jokic": 900,
        "Bam Adebayo": 750,
        "Domantas Sabonis": 600,
        "Karl Anthony-Towns": 500,
        # "Jonah": 500,
        # "Maile": 750,
        # "jake": 750,
        # "Ryan": 750,
        # "Max": 750
    }

    dict_sf = {
        "Lebron James": 1200,
        "Jimmy Butler": 1000,
        "Kawhi Leonard": 900,
        "Jaylen Brown": 750,
        "Zach Lavine": 600,
        # "Jonah": 500,
        # "Maile": 750,
        # "jake": 750,
        # "Ryan": 750,
        # "Max": 750
    }
    dict_pf = {
        "Giannis AntetoKounmpo": 1200,
        "Jayson Tatum": 1000,
        "Kevin Durant": 900,
        "Pascal Siakam": 750,
        "Zion Williamson": 600,
        # "Jonah": 500,
        # "Maile": 750,
        # "jake": 750,
        # "Ryan": 750,
        # "Max": 750
    }

    dict_sg = {
        "Shai Gilgeous-Alexander": 1200,
        "Donovan Mitchell": 1000,
        "Paul George": 900,
        "Devin Booker": 750,
        "DeMar Derozan": 600,
        "Lamelo Ball": 500,
        "David 'Tab Master' Doan": 100,
        "Sam '8 Mile' Waters": 100,
    }

    point_guard1_selection = True
    while point_guard1_selection:
        option1 = input(f'''
    {manager1.name}, Choose a Point Guard:

                    ROUND 1
    
    Luka Doncic       |	 - $1,200
    Ja Morant	      |  - $900
    James Harden	  |  - $750
    Damian Lillard	  |  - $600
    Steph Curry	      |  - $600
    Tyrese Haliburton |  - $600
    Kyrie Irving	  |  - $500
    Trae Young	      |  - $500


        ''')
        if option1 not in dict_pg:
            print("Choose a valid Point Guard")
        else:
            point_guard1 = dict_pg[option1]
            point_guard1_selection = False
            print(
                f"{manager1.name}'s Point Guard is {option1}, costing ${point_guard1}")

    point_guard2_selection = True
    while point_guard2_selection:
        option2 = input(f'''
        {manager2.name}, Choose a Point Guard:

                    ROUND 1
    

    Luka Doncic       |	 - $1,200
    Ja Morant	      |  - $900
    James Harden	  |  - $750
    Damian Lillard	  |  - $600
    Steph Curry	      |  - $600
    Tyrese Haliburton |  - $600
    Kyrie Irving	  |  - $500
    Trae Young	      |  - $500


        ''')
        if option2 == option1:
            print("Choose an undrafted point guard")
        else:
            point_guard2 = dict_pg[option2]
            point_guard2_selection = False
            print(
                f"{manager2.name}'s Point Guard is {option2}, costing ${point_guard2}")

    Remaining_budget_manager1 = (manager1.budget - point_guard1)
    Remaining_budget_manager2 = (manager2.budget - point_guard2)
    print(f"{manager1.name} you have ${Remaining_budget_manager1} remaining")
    print(f"{manager2.name} you have ${Remaining_budget_manager2} remaining")

    # add in rounds to show the player what round of pick this is.

    center1_selection = True
    while center1_selection:
        option3 = input(f'''
        {manager1.name}, Choose a Center:

                    ROUND 2
        

         Joel Embiid          | $1200
         Anthony Davis        | $1000
         Nikola Jokic         | $900
         Bam Adebayo          | $750
         Domantas Sabonis     | $600
         Karl Anthony-Towns   | $500

         
        ''')
        if option3 not in dict_center:
            print("Choose a valid Center")
        else:
            center1 = dict_center[option3]
            center1_selection = False
            print(
                f"{manager1.name}'s Center is {option3}, costing ${center1}")

    center2_selection = True
    while center2_selection:
        option4 = input(f'''
        {manager2.name}, Choose a Center:

                    ROUND 2

         Joel Embiid          | $1200
         Anthony Davis        | $1000
         Nikola Jokic         | $900
         Bam Adebayo          | $750
         Domantas Sabonis     | $600
         Karl Anthony-Towns   | $500


        ''')
        if option4 == option3:
            print("Choose an undrafted Center")
        else:
            center2 = dict_center[option4]
            center2_selection = False
            print(
                f"{manager2.name}'s Center is {option4}, costing ${center2}")

    Remaining_budget_manager1 -= center1
    Remaining_budget_manager2 -= center2
    print(f"{manager1.name} you have ${Remaining_budget_manager1} remaining.")

    print(f"{manager2.name} you have ${Remaining_budget_manager2} remaining")

    print(f''' 
    -----------------------------------------------
            AFTER ROUNDS 1 AND 2 HERE ARE THE TEAMS:

            {manager1.name}'s Team: Point Guard:{option1} | Center:{option3}
            {manager2.name}'s Team: Point Guard:{option2} | Center:{option4}

    -----------------------------------------------
    
    ''')

    sf1_selection = True
    while sf1_selection:
        option5 = input(f'''
                    ROUND 3

        {manager1.name}, Choose a Small Forward:


        Lebron James    | $1200
        Jimmy Butler    | $1000
        Kawhi Leonard   | $900
        Jaylen Brown    | $750
        Zach Lavine     | $600


        ''')
        if option5 not in dict_sf:
            print("Choose a valid Small Forward")
        else:
            small_forward1 = dict_sf[option5]
            sf1_selection = False
            print(
                f"{manager1.name}'s Small Forward is {option5}, costing ${small_forward1}")

    sf2_selection = True
    while sf2_selection:
        option6 = input(f'''
        {manager2.name}, Choose a Small Forward:

                    ROUND 3

        Lebron James    | $1200
        Jimmy Butler    | $1000
        Kawhi Leonard   | $900
        Jaylen Brown    | $750
        Zach Lavine     | $600


        ''')
        if option6 == option5:
            print("Choose an undrafted Small Forward")
        else:
            small_forward2 = dict_sf[option6]
            sf2_selection = False
            print(
                f"{manager2.name}'s Small Forward is {option6}, costing ${small_forward2}")

    Remaining_budget_manager1 -= small_forward1
    Remaining_budget_manager2 -= small_forward2
    print(f"{manager1.name} you have ${Remaining_budget_manager1} remaining.")

    print(f"{manager2.name} you have ${Remaining_budget_manager2} remaining")

    print("be mindful of how much you are spending")

    pf1_selection = True
    while pf1_selection:
        option7 = input(f'''
        {manager1.name}, Choose a Power Forward:

                    ROUND 4

        Giannis AntetoKounmpo  | $1200
        Jayson Tatum           | $1000
        Kevin Durant           | $900
        Pascal Siakam          | $750
        Zion Williamson        | $600

        
        ''')
        if option7 not in dict_pf:
            print("Choose a valid Power Forward")
        else:
            power_forward1 = dict_pf[option7]
            pf1_selection = False
            print(
                f"{manager1.name}'s Power Forward is {option7}, costing ${power_forward1}")

    pf2_selection = True
    while pf2_selection:
        option8 = input(f'''
        {manager2.name}, Choose a Power Forward:

                    ROUND 4

        Giannis AntetoKounmpo  | $1200
        Jayson Tatum           | $1000
        Kevin Durant           | $900
        Pascal Siakam          | $750
        Zion Williamson        | $600


        ''')
        if option8 == option7:
            print("Choose an undrafted Power Forward")
        else:
            power_forward2 = dict_pf[option8]
            pf2_selection = False
            print(
                f"{manager2.name}'s Power Forward is {option6}, costing ${power_forward2}")

    Remaining_budget_manager1 -= power_forward1
    Remaining_budget_manager2 -= power_forward2
    print(f"{manager1.name} you have ${Remaining_budget_manager1} remaining.")

    print(f"{manager2.name} you have ${Remaining_budget_manager2} remaining")

    print(f''' 
    -------------------------------------------------------------------------------------------------------------------------------
            AFTER ROUNDS 1,2,3 AND 4 HERE ARE THE TEAMS:

            {manager1.name}'s Team: Point Guard:{option1} | Center:{option3} | Small Forward: {option5} | Power Forward: {option7}
            {manager2.name}'s Team: Point Guard:{option2} | Center:{option4} | Small Forward: {option6} | Power Forward: {option8}

    -------------------------------------------------------------------------------------------------------------------------------

    
    ''')

    print(''' 
    --------------------------------------------------
            FINAL ROUND
    --------------------------------------------------
        
    ''')
    print(f"{manager1.name}'s budget for the final round is ${Remaining_budget_manager1} ")
    print(f"{manager2.name}'s budget for the final round is ${Remaining_budget_manager2} ")

    sg1_selection = True
    while sg1_selection:
        option9 = input(f'''
        {manager1.name}, Choose a Shooting Guard:

                    ROUND 5

        Shai Gilgeous-Alexander     | $1200
        Donovan Mitchell            | $1000
        Paul George                 | $900
        Devin Booker                | $750
        DeMar Derozan               | $600
        Lamelo Ball                 | $500
        David 'Tab Master' Doan     | $100
        Sam '8 Mile' Waters         | $100

        ''')
        if option9 not in dict_sg and dict_sg[option9] > Remaining_budget_manager1:
            print("Choose a valid Shooting Guard")
        # elif Remaining_budget_manager1 < 500:
        #     shooting_guard1 = dict_sg["David"]
        #     sg1_selection = False
        else:
            shooting_guard1 = dict_sg[option9]
            sg1_selection = False
            print(
                f"{manager1.name}'s Shooting Guard is {option9}, costing ${shooting_guard1}")

    sg2_selection = True
    while sg2_selection:
        option10 = input(f'''
        {manager2.name}, Choose a Shooting Guard:

                    ROUND 5

        Shai Gilgeous-Alexander     | $1200
        Donovan Mitchell            | $1000
        Paul George                 | $900
        Devin Booker                | $750
        DeMar Derozan               | $600
        Lamelo Ball                 | $500
        David 'Tab Master' Doan     | $100
        Sam '8 Mile' Waters         | $100

        ''')
        if option10 == option9 and dict_sf[option10] > Remaining_budget_manager2:
            print("Choose a valid Shooting Guard")
        # elif Remaining_budget_manager2 < 500:
        #     shooting_guard2 = dict_sg["Sam"]
        #     sg2_selection = False
        else:
            shooting_guard2 = dict_sg[option10]
            sg2_selection = False
            print(
                f"{manager2.name}'s Shooting Guard is {option10}, costing ${shooting_guard2}")

    Remaining_budget_manager1 -= shooting_guard1
    Remaining_budget_manager2 -= shooting_guard2
    print(f"{manager1.name} you have ${Remaining_budget_manager1} remaining.")

    print(f"{manager2.name} you have ${Remaining_budget_manager2} remaining")

    print(f''' 
    -------------------------------------------------------------------------------------------------------------------------------
            AFTER THE DRAFT HERE ARE THE TEAMS:

            {manager1.name}'s Team: Point Guard: {option1} | Center: {option3} | Small Forward: {option5} | Power Forward: {option7} | Shooting Guard: {option9}
            {manager2.name}'s Team: Point Guard: {option2} | Center: {option4} | Small Forward: {option6} | Power Forward: {option8} | Shooting Guard: {option10}

    -------------------------------------------------------------------------------------------------------------------------------

    
    ''')

    Custom_Team(manager_id=manager1.name, budget=hometown_budget1, Point_Guard_id=option1,
                Shooting_Guard_id=option3, Small_Forward_id=option5, Power_Forward_id=option7,
                Center_id=option9).add_to_db(session)
    Custom_Team(manager_id=manager2.name, budget=hometown_budget2, Point_Guard_id=option2,
                Shooting_Guard_id=option4, Small_Forward_id=option6, Power_Forward_id=option8,
                Center_id=option10).add_to_db(session)

    ptotal = 0
    p1list = [option1, option3, option5, option7, option9]
    for option in (p1list):
        player = Players.get_player_figures(session, option)
        ptotal_1 = player.Inside_scoring + player.Outside_Scoring + player.Defending + \
            player.Athleticism + player.Playmaking + player.Rebounding
        ptotal_3 = player.Inside_scoring + player.Outside_Scoring + player.Defending + \
            player.Athleticism + player.Playmaking + player.Rebounding
        ptotal_5 = player.Inside_scoring + player.Outside_Scoring + player.Defending + \
            player.Athleticism + player.Playmaking + player.Rebounding
        ptotal_7 = player.Inside_scoring + player.Outside_Scoring + player.Defending + \
            player.Athleticism + player.Playmaking + player.Rebounding
        ptotal_9 = player.Inside_scoring + player.Outside_Scoring + player.Defending + \
            player.Athleticism + player.Playmaking + player.Rebounding

    p2list = [option2, option4, option6, option8, option10]
    for option in (p2list):
        player = Players.get_player_figures(session, option)
        ptotal_2 = player.Inside_scoring + player.Outside_Scoring + player.Defending + \
            player.Athleticism + player.Playmaking + player.Rebounding
        ptotal_4 = player.Inside_scoring + player.Outside_Scoring + player.Defending + \
            player.Athleticism + player.Playmaking + player.Rebounding
        ptotal_6 = player.Inside_scoring + player.Outside_Scoring + player.Defending + \
            player.Athleticism + player.Playmaking + player.Rebounding
        ptotal_8 = player.Inside_scoring + player.Outside_Scoring + player.Defending + \
            player.Athleticism + player.Playmaking + player.Rebounding
        ptotal_10 = player.Inside_scoring + player.Outside_Scoring + player.Defending + \
            player.Athleticism + player.Playmaking + player.Rebounding
    # tst1 = 0
    # tst1 = option1 + option3 + option5 + option7 + option9
    sum_1 = ptotal_1 + ptotal_3 + ptotal_5 + ptotal_7 + ptotal_9
    sum_2 = ptotal_2 + ptotal_4 + ptotal_6 + ptotal_8 + ptotal_10

    # answer_final = True
    # while answer_final:
    #     input("Would you like to know the result?")
    #     if input != "Yes":
    #         print("Ya sure?")
    #     else:
    #         answer_final == False

    if sum_1 > sum_2:
        print(
            f"Congrats {manager1.name}! You have defeated {manager2.name} with a score of {sum_1} to {sum_2}!")
    else:
        print(
            f"Congrats {manager2.name}! You have defeated {manager1.name} with a score of {sum_2} to {sum_1}")

    print("Thanks for playing NBA MANAGER!")

    saved_game = True
    while saved_game:
        input("Would you like to save your game? (Yes or No)")
        if input == "Yes":
            saved_game = False
        else:
            # delete functionality which will take the team off of the custom team table
            print("Thanks for playing!")

            # Loop through playerlist
            # Get the individual players
            # tst1 +=
            # Total_score_team1 = (manager1.Outside_Scoring + manager1.Inside_Soring +
            #                      manager1.Defending + manager1.Athleticism + manager1.Playmaking + manager1.Rebounding)
            # Total_score_team2 = (manager2.Outside_Scoring + manager2.Inside_Soring +
            #                      manager2.Defending + manager2.Athleticism + manager2.Playmaking + manager2.Rebounding)

            # Remaining_budget_manager1 = Managers(
            #     manager1.budget).get_manager(hometown_budget1 - point_guard1)

            # Remaining_budget_manager2 = hometown_budget2 - point_guard2
            # print(f"{manager1.name} you have ${Remaining_budget_manager1} remaining")

            # print(f'{manager2} you have ${Remaining_budget_manager2} remaining.')

            # I want to access the cost of each player to give the manager an idea of how much money they
            # have remaining for other players

            # at the end I'd like to query through and print out the teams that are associated with each manager

            # if option2 in dict:
            #     hometown_budget2 = dict[option2]
            #     hometown_selection2 = False
            #     Managers(name=manager2, budget=option1,
            #              hometown=hometown_budget2).add_to_db(session)
            #     print(
            #         f" {manager2}, your hometown is {option2} and your budget to build a roster is ${hometown_budget2}")
            # else:
            #     print("Pick a valid city")
