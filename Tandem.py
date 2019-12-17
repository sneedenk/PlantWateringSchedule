#!python3
"""Sumbission for Tandem Aprentice 2019 Challenge. Will add more later."""

import json
from datetime import date, timedelta

#submission date is 12/16/2019; next Monday is 12/23/2019
start_date = date(2019, 12, 23)

# read file; store json data
with open('Apprentice_WeGrowInTandem_Data.json', 'r') as my_file:
    raw_data = my_file.read()

json_data = json.loads(raw_data)
plant_data = {}

# =============================================================================
# Extracts the int value of 'water_after'.  Then plants are saved in plant_data
# by name.  Each plant knows when it needs to be watered next and how many
# days later it needs to be watered again
# =============================================================================
for plant in json_data:
    space_index = plant['water_after'].find(" ")
    water_after = int(plant['water_after'][:space_index])
    next_water_day = 0
    plant_data[plant['name']] = [next_water_day, water_after]

schedule = []

#For each day in the next 12 weeks
for day in range(0,7*12):
    todays_watering = []
    # ========================================================================
    # For each plant, check if it needs to be watered today.  If so, add it to 
    # todays_watering list and update the next day it needs to be watered.
    # ========================================================================
    for plant, data in plant_data.items():
        if data[0] == day: #data[0] <- next day the plant needs to be watered
            todays_watering.append(plant)
            #weekend adjustments
            if (data[0] + data[1]) % 7 == 5: #Saturday
                data[0] += data[1] - 1 #data[1] <- water_after from json
            elif (data[0] + data[1]) % 7 == 6: #Sunday
                data[0] += data[1] + 1
            else: #weekdays
                data[0] += data[1]
    
    #Add fillers for the weekends, otherwise add todays_waterin to the schedule.
    if day % 7 == 5:
        schedule.append([])
    elif day % 7 == 6:
        schedule.append([])
    else:
        schedule.append(todays_watering)

# =============================================================================
# Prints the full daily watering schedule from 12-23-2019 to 3-15-2020.  
# 
# The process begins by converting the current day into a timedelta and 
# adding that delta to the hard-coded start_date to get the current date, 
# which is printed.  Then iterate over the schedule for the current day and 
# add each plant to todays_plants, a comma-separated string.  This allows for 
# single line of concise output.
# =============================================================================
def printFullSchedule():
    for day in range(0,7*12):
        todays_plants = ""
        delta = timedelta(day)
        todays_date = start_date + delta
        #reorganize the date to MM-DD-YYYY and print it
        print(str(todays_date.month) + "-" + str(todays_date.day) + "-" + str(todays_date.year))
        for curPlant in schedule[day]:
            todays_plants += ", " + curPlant
        print(todays_plants[2:])    #drop the initial ", "
        print()

# =============================================================================
# Prints the watering schedule of a single day, as requested by the user.
# 
# Prompts the user for a month formatted M or MM, day formatted D or DD, and 
# year formatted YYYY.  Inputs are casted to int, so any non-integer input 
# throws a ValueError exception and the user is prompted to input the request
# again.  Upon receiving integer input, the ints are converted to a date. If
# the user enters month integers outside of [1-12] or day integers <1 or more 
# than the number of days in the designated month and year (2020 is a Leap 
# Year!), then another ValueError exception is thrown and the user is prompted 
# to input a new legal date.  Once an acceptable date is input, it is then 
# used to calculate a timedelta for how far the requested date is from the 
# hard-coded start_date.  If the date is before the start date or more than
# 84 days after it, it is considered illegal input, as it is outside the 12
# week scheduling period.  In this case, the user is reminded of the legal date
# range and prompted to input a new legal date.
#
# Given appropriate input from the user, the user's date is used to compute a
# timedelta, which is the number of days away from the start_date it is.  Then,
# the list of plants to water that day can be looked up using the timedelta.  
# The size of the resulting list of plants is used to print how many plants 
# there are to water that day, followed by a newline separated list of the plants.
# =============================================================================
def printDateSchedule():
    print("Enter the date you want to see the schedule.")
    while True:
        while True:
            try:
                user_month = int(input("Month (M or MM): "))
                break
            except ValueError:
                print("You have to enter numbers as M or MM. Month: ")  # Catch int() exception
        while True:
            try:
                user_day = int(input("Day (D or DD): "))
                break
            except ValueError:
                print("You have to enter numbers as D or DD. Day: ")  # Catch int() exception
        while True:
            try:            
                user_year = int(input("Year (YYYY): "))
                break
            except ValueError:
                print("You have to enter numbers as YYYY. Year: ")  # Catch int() exception
        try:
            user_date = date(user_year, user_month, user_day)
            user_delta = user_date - start_date
            if user_delta.days >= 0 and user_delta.days < 84:
                print("There are " + str(len(schedule[user_delta.days])) + " plants to water on " + str(user_month) + "-" + str(user_day) + "-" + str(user_year) + ".")
                for todays_plants in schedule[user_delta.days]:
                    print(todays_plants)
                break
            else:
                print("Illegal date input. Date must be between 12-23-2019 and 3-15-2020. Try another date: ")
        except ValueError: 
            print("Illegal date input. Try another date: ")
        

# =============================================================================
# Prompts the user to enter a 1 or a 2.  1 prints the full schedule.  2 prompts
# the user for a date for which to check the watering schedule.
#
# Again the input is casted to int, so any non-integer input throws a 
# ValueError and prompts the user again to input a 1 or a 2.  If the user 
# inputs an integer other than a 1 or 2, they are looped back to the original 
# prompt for a 1 or a 2.
# =============================================================================
print("Enter 1 to see the full schedule or 2 to check the schedule for a specific date.")
valid_options = [1, 2]
while True:
    try:
        task = int(input("Enter 1 or 2: "))
        if task in valid_options:
            break
    except ValueError:
        print("You have to enter 1 or 2.")  # Catch int() exception
        
if task == 1:
    printFullSchedule()
elif task == 2:
    printDateSchedule()
