from classes.Managers import Managers
from classes.Players import Players
from classes.custom_team import Custom_Team


def hometown_selection(session, manager1, manager2):
    option1 = None
    option2 = None
    list = ["Denver", "Phoenix", "Los Angeles",
            "Miami", "Memphis", "1", "2", "3", "4", "5"]
    dict = {
        "Denver": 5000,
        "1": 5000,
        "Phoenix": 4500,
        "2": 4500,
        "Los Angeles": 3750,
        "3": 3750,
        "Miami": 4500,
        "4": 4500,
        "Memphis": 3500,
        "5": 3500,
        "New York": 6000,
        "6": 6000,
        "Boston": 6500,
        "7": 6500,
        "San Francisco": 6000,
        "8": 6000,
        "Detroit": 4500,
        "9": 4500,
        "Toronto": 5500,
        "10": 5500,


    }
    hometown_budget1 = None
    hometown_budget2 = None
    hometown_selection1 = True
    hometown_selection2 = True
    while hometown_selection1:
        print(f"{manager1} pick a hometown")
        option1 = input(''' 
            Choose a Hometown
            1) Denver
            2) Phoenix
            3) Los Angeles
            4) Miami
            5) Memphis
            6) New York
            7) Boston
            8) San Francisco
            9) Detroit
            10) Toronto
            
            ''')
        if option1 in dict:
            hometown_budget1 = dict[option1]
            # hometown_budget1.add_budget(session, manager1)
            hometown_selection1 = False
            Managers(name=manager1, budget=hometown_budget1,
                     hometown=option1).add_to_db(session)

            print(
                f" {manager1}, your hometown is {option1} and your budget to build a roster is ${hometown_budget1}")

        else:
            print("Pick a City from the List")

    while hometown_selection2:
        print(f"{manager2}: pick a hometown")
        option2 = input(''' 
            Choose a Hometown
            1) Denver
            2) Phoenix
            3) Los Angeles
            4) Miami
            5) Memphis
            6) New York
            7) Boston
            8) San Francisco
            9) Detroit
            10) Toronto
            
            ''')

        if option2 in dict and option2 != option1:
            hometown_budget2 = dict[option2]
            hometown_selection2 = False
            Managers(name=manager2, budget=hometown_budget2,
                     hometown=option2).add_to_db(session)
            print(
                f" {manager2}, your hometown is {option2} and your budget to build a roster is ${hometown_budget2}")
        else:
            print("Pick a valid city")
# update function that will add $250 to the budget if Jordan too something personally
    Bonus = input(
        f"{manager1}, did you do something that Michael Jordan took personally? (the answer is always yes)")
    if Bonus == "yes":
        session.query(Managers).update({
            Managers.budget: Managers.budget + 250
        })

        # add home vs away functionality
