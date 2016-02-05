"""
birthday.py
Author: Daniel Wilson
Credit: SSupattapone
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

n = input("Hello, what is your name? ")
m = input("Hi " + n + ", what was the name of the month you were born in? ")
y = float(input("And what year were you born in, " + n + "? "))
d = float(input("And the day? "))


if m in ["December", "January", "February"] :
    Season = ("winter")
elif m in ["March", "April", "May"]:
    Season = ("spring")
elif m in ["June", "July", "August"]:
    Season = ("summer")
elif m in ["September", "October", "November"]:
    Season = ("fall")
    

    
if y >= 1980 and y <= 1989 :
    years = ("the eighties")
elif y >= 1990 and y <= 1999 :
    years = ("the nineties")
elif y >= 2000 and y <= 2020 :
    years = ("two thousands")
elif y < 1980 :
    years = ("the STONE AGE")


if m == month_name [todaymonth] and d == todaydate :
    print("Happy birthday!")
elif d == 31 and m == "October" :
    print("You were born on Halloween!")
else :
    print(n + ", you are a " + Season + " baby of the " + years + ".")
    
    
    