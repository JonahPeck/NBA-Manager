from classes.Managers import Managers
from classes.Players import Players
from classes.custom_team import Custom_Team


def hometown_selection(session, manager1, manager2):
    option1 = None
    option2 = None
    list = ["Denver", "Phoenix", "Los Angeles",
            "Miami", "Memphis", "1", "2", "3", "4", "5"]
    dict = {
        "Denver": 1000,
        "1": 1000,
        "Phoenix": 2000,
        "2": 2000,
        "Los Angeles": 3000,
        "3": 3000,
        "Miami": 2500,
        "4": 2500,
        "Memphis": 2200,
        "5": 2200

    }
    print(f"{manager1} pick a hometown")
    option1 = input(''' 
        Choose a Hometown
        1) Denver
        2) Phoenix
        3) Los Angeles
        4) Miami
        5) Memphis
        
        ''')
    hometown_budget1 = None
    hometown_budget2 = None
    hometown_selection1 = True
    hometown_selection2 = True
    while hometown_selection1:
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
            
            ''')

        if option2 in dict:
            hometown_budget2 = dict[option2]
            hometown_selection2 = False
            Managers(name=manager2, budget=hometown_budget2,
                     hometown=option2).add_to_db(session)
            print(
                f" {manager2}, your hometown is {option2} and your budget to build a roster is ${hometown_budget2}")
        else:
            print("Pick a valid city")
