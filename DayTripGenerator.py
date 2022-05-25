import random

destination_list= ['Aspen', 'Barbados', 'Hong Kong', 'Amsterdam', 'Dubai']
transportation_list = ['Camel', 'Rolls Royce', 'Moped', 'Taxi', 'Uber']
restaurant_list = ['Aspen Snowmass', 'The Cliff', 'the Chairtown', 'Buelings', 'Certo']
entertainment_list = ['Skiing', 'Music festival', 'Go-karting', 'Repository tour', 'Visit Aquarium & underwater zoo'] 

def destination():
    print('Welcome to DayTrip generator, please use lowercase y or n for all selections.')
    rand_dest = random.choice(destination_list)
    user_input = input(f'Would you like to go to {rand_dest}? y/n ')
    while user_input != 'y':
        rand_dest = random.choice(destination_list)
        user_input = input(f'how about {rand_dest}? y/n ')
    return rand_dest
destination()

def transportation():
    rand_transpo = random.choice(transportation_list)
    user_input = input(f'How would you like to travel by {rand_transpo}? y/n ')
    while user_input != 'y':
        rand_transpo = random.choice(transportation_list)
        user_input = input(f'okay what about {rand_transpo}? y/n ')
    return rand_transpo
transportation()

def restaurant():
    rand_rest = random.choice(restaurant_list)
    user_input = input(f'You will be dining at {rand_rest} is that okay? y/n ')
    while user_input != 'y':
        rand_rest = random.choice(restaurant_list)
        user_input = input(f'maybe {rand_rest} is better for you. y/n ')
    return rand_rest
restaurant()

def entertainment():
    rand_ent = random.choice(entertainment_list)
    user_input = input(f'would you like to go to {rand_ent}? y/n ')
    while user_input != 'y':
        rand_ent = random.choice(entertainment_list)
        user_input = input(f'alright maybe this is a better option {rand_ent} y/n')
    return rand_ent
entertainment()
   
def finalize_trip(destination, transportation, entertainment, restaurant):
    print(f'You will be going to {destination} moving around by {transportation}')
    print(f"While you are at {destination} , you will be dining at {restaurant} and enjoying {entertainment} ")
    user_input = input(f"Are you happy with these choices? y/n: ")
    if user_input == "y":
        print('Have a great day trip!')
    elif user_input == 'n':
        finalize_trip()
    
def day_trip():
    finalize_destination = destination()
    finalize_transportation = transportation()
    finalize_entertainment = entertainment()
    finalize_restaurant = restaurant()
    finalize_trip(finalize_destination, finalize_transportation, finalize_entertainment, finalize_restaurant)

day_trip()

