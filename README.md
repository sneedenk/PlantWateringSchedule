The purpose of this project is to create a 12-week plant watering schedule for the Tandem office. 
There are data about the plants in the office and how often they need to be watered in 
Apprentice_WeGrowInTandem_Data.json. For more specific instructions as to the goals of this script, 
see Tandem_SEApprentice_Challenge_2019.pdf. The main software for this project can be found at:
https://github.com/sneedenk/Tandem_App/blob/master/Tandem.py.

Tandem.py was programmed in Python 3.7.4 and Anaconda version 4.8.0, although the only dependencies 
are json and datetime, so any version of Python3 that can use both packages ought to work. Tandem.py 
does not have any special run instructions. As a command-line tool, you can run it from your choice 
of Python3 compatible environments. It does not take additional command-line arguments.

Using Tandem.py is self-explanatory, just follow the prompts as given. Tandem.py has two main modes 
of functionality. (1) You can print an entire 12-week watering schedule or (2) you can print a 
single date's watering schedule. Upon starting Tandem.py enter either 1 or 2, as prompted, to 
select your preferred usage. Selecting 1 immediately prints the entire 12-week schedule, while
selecting 2 further prompts the user to enter date information. Given valid date inputs, meaning
legal dates (no 0th month or 32nd day of the month, and other numbers you won't find on a calendar 
and no non-integer inputs) within 12 weeks of the start date, the plants to water that day are 
printed.

Possible future features that would have been nice to include would be a graphcial user 
interface and additional options for dates to display, such as printing a week's worth of 
watering schedules.
