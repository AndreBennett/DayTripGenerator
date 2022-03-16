

import random
destination_list= 'Aspen', 'Barbados', 'Hong Kong', 'Amsterdam', 'Dubai'
transportation_list = 'Camel', 'Rolls Royce', 'Moped', 'Taxi', 'Uber'
resturant_list = 'Aspen Snowmass', 'The Cliff', 'the Chairtown', 'Buelings', 'Certo',
entertainment_list = 'Skiing', 'Music festival', 'Go-karting', 'Repository tour', 'Visit Aquarium & underwater zoo' 


def Destination():
    print("You were given ", random.choice(destination_list))
    Destination = input('Are you happy with your destination? y/n ')
    if Destination == 'y':
        print('Great Choice')
    if Destination == 'n':
        print('Another option is ', random.choice(destination_list))
    Destination = input('Is that a better option for you? y/n ')
    if Destination == 'y':
        print("Okay let's get you some transportation")
    if Destination =='n':
        print('Okay we have', random.choice(destination_list))
    Destination = input('Are you happy with that option? y/n ')
    if Destination == 'y':
        print('Perfect lets move on. ')
    if Destination == 'n':
        print('Okay how about', random.choice(destination_list))   
    Destination = input('Hopefully this one works for you. y/n ')
    if Destination == 'n':
        print('Alright we can try again. ', random.choice(destination_list))
   

Destination()
def Transportation():
    print('Now that we have your destination, lets figure out what your transportation will be. ', random.choice(transportation_list))
    Transportation = input('Did that option work for you? y/n' )
    if Transportation == 'y':
        print('ok perfect')
    if Transportation == 'n':
        print('Okay lets see what else I have for you', random.choice(transportation_list))
    Transportation = input('Is that a better option? y/n ')
    if Transportation == 'y':
        print('Good I am glad that works for you')
    if Transportation == 'n':
        print('Okay no problem, we also have a', random.choice(transportation_list)) 
    Transportation = input('Is that a better option for you? y/n ')
    if Transportation == 'y':
        print("Perfect glad we took care of that for you")
    if Transportation == 'n':
        print('No problem we have other options, how about a ', random.choice(transportation_list))
    Transportation = input('Will that one work for you? y/n ')
    if Transportation == 'y':
        print('Perfect')
    if Transportation == 'n':
        print('Alright we will try again ', random.choice(transportation_list))
Transportation()
def Resturant():
    print('Alright we have your location and transportation taken care of lets figure out dinner. ', random.choice(resturant_list))
    Resturant = input('Hopefully that works for you. y/n ')
    if Resturant == 'y':
        print('glad we were able to solve that quickly ')
    if Resturant == 'n':
        print('Alright no worries we have other options as well', random.choice(resturant_list))
    Resturant = input('Does that sound better to you? y/n ')
    if Resturant == 'y':
        print('That is good to know lets continue')
    if Resturant == 'n':
        print('Alright lets give it another try ', random.choice(resturant_list))
    Resturant = input('How about that meal? y/n ')
    if Resturant == 'y':
        print('Good glad you found a good meal')
    if Resturant == 'n':
        print('Okay thats fine we can keep searching', random.choice(resturant_list))
    Resturant = input('Hopefully that meal is what you want y/n ')
    if Resturant == 'y':
        print('Good lets move on to an activty')
    if Resturant == 'n':
        print('We can try one more time', random.choice(resturant_list))
Resturant()
def Entertainment():
    print('Okay lets finish this out on a good note, how does ', random.choice(entertainment_list), 'sound?' )
    Entertainment = input('hopefully its a yes? y/n ')
    if Entertainment == 'y':
        print('So glad we were able to solve that quickly')
    if Entertainment == 'n':
        print('No worries we will find something for you to do. How about?', random.choice(entertainment_list))
    Entertainment = input('Will that be a yes or no? y/n' )
    if Entertainment == 'y':
        print('Great good to hear')
    if Entertainment == 'n':
        print('Alright lets keep searching, how about?', random.choice(entertainment_list))
    Entertainment = input('Surely that was the one right? y/n' )
    if Entertainment == 'y':
        print('Cool glad we figured it out')
    if Entertainment == 'n':
        print('Thats fine we have other options such as', random.choice(entertainment_list))
    Entertainment = input('Will that one work for you? y/n ')
    if Entertainment == 'y':
        print('Glad we got that handled')
    if Entertainment == 'n':
        print('Alright lets try one more time', random.choice(entertainment_list))
      
# print(random.choice(transportation_list))
# print(random.choice(resturant_list))
# print(random.choice(entertainment_list))


# def tripoptions(daytripoptions):
#     user_input = input(f'Where would you like to take a trip to? {daytrip}')
#     lowered_input = user_input.lower()
#     for options in daytripoptions:
#         if options == lowered_input:
#             print(options)
# tripoptions(daytrip)

# def transpo(transpooptions):
#     user_input = input(f'What type of transportation would you like? {transportation}')
#     lowered_input = user_input.lower()
#     for options2 in transpooptions:
#         if options2 == lowered_input:
#             print(options2)
# transpo(transportation)

# def food(foodoptions):
#     user_input = input(f'Where would you like to eat? {resturant}')
#     lowered_input = user_input.lower()
#     for options3 in foodoptions:
#         if options3 == lowered_input:
#             print(options3)
# food(resturant)

# def enjoyment(entertainmentoptions):
#     user_input = input(f'What would you like to do today? {entertainment}')
#     lowered_input = user_input.lower()
#     for options4 in entertainmentoptions:
#         if options4 == lowered_input:
#             print(options4)
# enjoyment(entertainment)

# trip_option1 = input('Would you like to go to Dubai? y/n ')
# trip_option2 = input('Would you like to go to Amsterdam? y/n ')
# trip_opgion3 = input('Would you like to go to Hong Kong? y/n ')
# trip_option4 = input('Would you like to go to Barbados? y/n ')
# trip_option5 = input('Would you like to go to Aspen? y/n ')

# daytrip = destination_list, transportation_list, resturant_list, entertainment_list
# destination = random.choice(random.choices(daytrip, weights=map(len, daytrip))[0])
# print(destination)  



# def dubai():
#     Dubai = input('Would you like to go to Dubai? y/n ')
#     if  Dubai == 'y':
#         print('You picked Dubai ')
#     else:
#         print('Okay we have other options ')
#     Amsterdam = input('What about amsterdam? y/n ')

#     Transportation = input('Would you like to ride a camel today? y/n ')
#     if Transportation == 'y':
#         print('Great you picked a camel')
#     if Transportation == 'n':
#         print('No worries we have more options.')
    
#     if Amsterdam == 'y':
#         print('Great you picked Amsterdam' )
#     if Amsterdam == 'n':
#         print('Alright how does Hong Kong sound? ')
#     Hong_Kong = input('y/n ')
#     if Hong_Kong == 'y':
#         print('Great I think you will love it there ')
#     if Hong_Kong == 'n':
#         print('Alright what about Barbados? ')
#     Barbados = input('y/n ')
#     if Barbados == 'y':
#         print('Perfect I hope you really enjoy your stay')
#     if Barbados == 'n':
#         print("Alright, hate that we couldn't make that work for you. What about Aspen? ")
#     Aspen = input('y/n ')
#     if Aspen == 'y':
#         print('You picked lovely Aspen. ')
#     if Aspen == 'n':
#         print('Please try again')

#     transportation = input('Would you like to ride a camel tody? y/n ')
#     if transportation == 'y':
#         print('Great you picked a Camel' )
#     elif transportation == 'n':
#         print('Alright we have other options available.' )
#     Resturant_choice1 = input('Would you like to dine at certo tonight? y/n ')
#     if Resturant_choice1 == 'y':
#         print('Good choice ')
#     elif Resturant_choice1 == 'n':
#         print('Thats fine we have other options' )
#     def Amsterdam():
#         Amsterdam_input = input('Would you like to go to Amsterdam? y/n ')
#         if Amsterdam_input == 'y':
#             print('Great you picked Amsterdam ')
#         elif Amsterdam_input == 'n':
#             print('Dang will try again ')
#     Amsterdam()
# dubai()

# def Hong_Kong():
#     Hong_Kong_input = input('Would you like to go to Hong Kong? y/n ')
#     if Hong_Kong_input == 'y':
#         print('You picked Hong Kong ')
#     elif Hong_Kong_input == 'n':
#         print('Will try again. ')
# Hong_Kong()

# def Barbados():
#     Barbados_input = input('Would you like to take a caribbean trip to Barbados? y/n ')
#     if Barbados_input == 'y':
#         print('You selected the lovely island of Barbados' )
#     elif Barbados_input == 'n':
#         print('Dang you are missing out' )
# Barbados()

# def Aspen():
#     Aspen_input = input('Would you like to take a trip to Aspen? y/n ')
#     if Aspen_input == 'y':
#         print('Perfect you selected Aspen ')
#     elif Aspen_input == 'n':
#         print('We ran out of options')
# Aspen()
