def hotel_cost(nights):
    return 140*nights
def plan_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Pittsburgh" == city:
        return 222
    elif "Tampa" == city:
        return 220
    elif "los Angles" == city:
        return 475
    
def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days-20
    else: 
        return 40*days

def trip_cost(city, days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plan_ride_cost(city) +spending_money
print("The total trip cost to tampa is", trip_cost("Tampa",6,500))