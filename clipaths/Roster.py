from classes.Players import Players
from classes.Managers import Managers


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
        "Jonah": 500,
        "Maile": 750,
        "jake": 750,
        "Ryan": 750,
        "Max": 750
    }
    dict_center = {
        "Joel Embiid": 1200,
        "Anthony Davis": 1000,
        "Nikola Jokic": 900,
        "Bam Adebayo": 750,
        "Domantas Sabonis": 600,
        "Karl Anthony-Towns": 500,
        "Jonah": 500,
        "Maile": 750,
        "jake": 750,
        "Ryan": 750,
        "Max": 750
    }

    dict_sf = {
        "Lebron James": 1200,
        "Jimmy Butler": 1000,
        "Kawhi Leonard": 900,
        "Jaylen Brown": 750,
        "Zach Lavine": 600,
        "Jonah": 500,
        "Maile": 750,
        "jake": 750,
        "Ryan": 750,
        "Max": 750
    }
    dict_pf = {
        "Giannis AntetoKounmpo": 1200,
        "Jayson Tatum": 1000,
        "Kevin Durant": 900,
        "Pascal Siakam": 750,
        "Zion Williamson": 600,
        "Jonah": 500,
        "Maile": 750,
        "jake": 750,
        "Ryan": 750,
        "Max": 750
    }

    dict_sg = {
        "Shai Gilgeous-Alexander": 1200,
        "Donovan Mitchell": 1000,
        "Paul George": 900,
        "Devin Booker": 750,
        "DeMar Derozan": 600,
        "Lamelo Ball": 500,
        "Jonah": 500,
        "Maile": 750,
        "jake": 750,
        "Ryan": 750,
        "Max": 750
    }

    point_guard1_selection = True
    while point_guard1_selection:
        option1 = input(f'''
    {manager1.name}, Choose a Point Guard:
    (testing data)
    Jonah - 500
    Maile - 750
    jake - 750
    Ryan - 750
    Max -750


    Luka Doncic       |	  Dallas, Mavericks	        - $1,200
    Ja Morant	      |   Memphis, Grizzlies	    - $900
    James Harden	  |   Philly, 76ers	            - $750
    Damian Lillard	  |   Portland, Trailblazers	- $600
    Steph Curry	      |   Golden State, Warriors	- $600
    Tyrese Haliburton |   Indiana, Pacers	        - $600
    Kyrie Irving	  |   Dallas, Mavericks	        - $500
    Trae Young	      |   Atlanta, Hawks	        - $500


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
    (testing data)
    Jonah - 500
    Maile - 750
    jake - 750
    Ryan - 750
    Max -750


    Luka Doncic       |	  Dallas, Mavericks	        - $1,200
    Ja Morant	      |   Memphis, Grizzlies	    - $900
    James Harden	  |   Philly, 76ers	            - $750
    Damian Lillard	  |   Portland, Trailblazers	- $600
    Steph Curry	      |   Golden State, Warriors	- $600
    Tyrese Haliburton |   Indiana, Pacers	        - $600
    Kyrie Irving	  |   Dallas, Mavericks	        - $500
    Trae Young	      |   Atlanta, Hawks	        - $500


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
    (testing data)
    Jonah - 500
    Maile - 750
    jake - 750
    Ryan - 750
    Max -750

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
    (testing data)
    Jonah - 500
    Maile - 750
    jake - 750
    Ryan - 750
    Max -750
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
        {manager1.name}, Choose a Small Forward:
    (testing data)
    Jonah - 500
    Maile - 750
    jake - 750
    Ryan - 750
    Max -750

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
    (testing data)
    Jonah - 500
    Maile - 750
    jake - 750
    Ryan - 750
    Max -750
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

    sf1_selection = True
    while sf1_selection:
        option5 = input(f'''
        {manager1.name}, Choose a Small Forward:
    (testing data)
    Jonah - 500
    Maile - 750
    jake - 750
    Ryan - 750
    Max -750

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
    (testing data)
    Jonah - 500
    Maile - 750
    jake - 750
    Ryan - 750
    Max -750
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
