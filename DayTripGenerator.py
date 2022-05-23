import random

destination_list= ['Aspen', 'Barbados', 'Hong Kong', 'Amsterdam', 'Dubai']
transportation_list = ['Camel', 'Rolls Royce', 'Moped', 'Taxi', 'Uber']
restaurant_list = ['Aspen Snowmass', 'The Cliff', 'the Chairtown', 'Buelings', 'Certo']
entertainment_list = ['Skiing', 'Music festival', 'Go-karting', 'Repository tour', 'Visit Aquarium & underwater zoo'] 

def daytrip(destination_list):
    print('Welcome to DayTrip generator, please use lowercase y or n for all selections.')
    print(random.choice(destination_list),'will be where you are going, will that work for you?')
    destination = input ('y/n ')
    while destination == 'n':
        print('How does', random.choice(destination_list),'sound y/n')
        destination = input ('')
        if destination == 'y':
            print('Great lets find some transportation for you')
    return destination
daytrip(destination_list)

def transportation(transportation_list):
    print(random.choice(transportation_list), 'will be your method of travel')
    transportation = input('Does that option work for you? y/n ')
    while transportation == 'n':
        print('How about', random.choice(transportation_list))
        transportation = input('y/n ')
        if transportation == 'y':
            print('Perfect now to get some food')
    return transportation
transportation(transportation_list)

def restaurant(restaurant_list):
    print(random.choice(restaurant_list), 'Will be where you dine tonight, is that okay with you?')
    restaurant = input('y/n ')
    while restaurant == 'n':
        print("Alright let's try again", random.choice(restaurant_list), 'how about that?')
        restaurant = input('y/n ')
        if restaurant == 'y':
            print('Cool one more step to complete this trip')
    return restaurant
restaurant(restaurant_list)

def entertainment(entertainment_list):
    print(random.choice(entertainment_list), 'Will be your entertainment for the night')
    entertainment = input('will that work for you? y/n ')
    while entertainment == 'n':
        print('No worries how about', random.choice(restaurant_list))
        entertainment = input('y/n ')
        if entertainment == 'y':
            print("Great that wraps up this trip for you, let's finalize the details")
    return entertainment
entertainment(entertainment_list)
   
def finaltripdetails():
    finaldest = daytrip(destination_list)
    finaltranspo = transportation(transportation_list)
    finalentertainment = entertainment(entertainment_list)
    finalrestaurant = restaurant(restaurant_list)
    print('Your trip has been finalized lets confirm the details')
    print('Your destination is', finaldest, 'your transportation is', finaltranspo, 'your entertainment is', finalentertainment, 'and your meal is from', finalrestaurant)
    finaltrip = input('Does this work for you? y/n ')
    if finaltrip == 'y':
        print('Perfect enjoy your trip')
    else:
        print('Alright we can try again')

finaltripdetails()