def hometown_selection(session):
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
    if option1 in dict:
        hometown_budget1 = dict[option1]
        print(
            f" Manager #1 your hometown is {option1} and your budget to build a roster is {hometown_budget1}")

    else:
        print("Pick a City from the List")
    # print(f"Your budget to build a roster is {option1}")
    # I want this to return the budget that the manager has based on the
    # city they chose
