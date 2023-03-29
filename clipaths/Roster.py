def roster_selection(session, manager1, manager2, hometown_budget1, hometown_budget2):
    roster_count = 0
    option1 = None
    option2 = None
    option3 = None
    option4 = None
    option5 = None
    option6 = None
    option7 = None
    option8 = None
    option9 = None
    option10 = None
    point_guard1 = None
    point_guard2 = None
    center1 = None
    center2 = None
    small_forward1 = None
    small_forward2 = None
    power_forward1 = None
    power_forward2 = None
    shooting_guard1 = None
    shooting_guard2 = None

    print("Let's build your rosters")
    print(f"{manager1}, choose a Point Guard")

    roster_list = ["Jonah", "Maile", "jake", "Ryan", "Max", "Luka Doncic", "Ja Morant", "James Harden", "Damian Lillard", "Steph Curry",
                   "Tyrese Haliburton", "Kyrie Irving", "Trae Young"]
    dict = {
        "Luka Doncic": 1200,
        "Ja Morant": 900,
        "James Harden": 750,
        "Damian Lillard": 600,
        "Steph Curry": 600,
        "Tyrese Haliburton": 600,
        "Kyrie Irving": 500,
        "Trae Young": 500,
        "Jonah": 500,
        "Maile": 750,
        "jake": 750,
        "Ryan": 750,
        "Max": 750


    }

    input(f'''
    {manager1}, Choose a Point Guard:
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
    if point_guard1 in dict:
        point_guard1 = dict[option1]
        print(f"{manager1}'s Point Guard is {point_guard1}")

    input(f'''
   {manager2}, Choose a Point Guard:
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
    while point_guard2 == point_guard1:
        if point_guard2 != point_guard1:
            point_guard2 = dict[option2]
        else:
            print("Pick another point guard")

    # if option2 in dict:
    #     hometown_budget2 = dict[option2]
    #     hometown_selection2 = False
    #     Managers(name=manager2, budget=option1,
    #              hometown=hometown_budget2).add_to_db(session)
    #     print(
    #         f" {manager2}, your hometown is {option2} and your budget to build a roster is ${hometown_budget2}")
    # else:
    #     print("Pick a valid city")
