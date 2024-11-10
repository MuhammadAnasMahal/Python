def weather_condition(season):
    if season == "Autumn":
        print("The weather is medium in autumn")
    elif season == "Spring":
        print("The weather is good")
    else:
        print("Wron input")
season = input("Type the season")
weather_condition(season)