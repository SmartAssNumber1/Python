from datetime import datetime
from calendar import monthrange
# get current datetime
now = datetime.now()
# get users input
given_date = input("Give a date:")
# split the date
day1 = given_date[0:2]
month1 = given_date[3:5]
year1 = given_date[6:10]
day2 = now.day
# print the result
print("The difference is: " + str(abs(int(day1) - int(day2))) +
      " days, " + str(now.hour) + " hours and " + str(now.second) + " seconds\n" +
      "The days of the specified month are: " + str(monthrange(int(year1), int(month1))[1]))
