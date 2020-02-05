import random
import time

from enum import Enum


class Color(Enum):
    green = 1
    red = 2


class Traffic_lamp:
    def __init__(self, name, color, cars):
        self.name = name
        self.color = color
        self.cars = cars


# create the 3 objects
t1 = Traffic_lamp("(1)", Color.red, random.randint(0, 30))
t2 = Traffic_lamp("(2)", Color.red, random.randint(0, 30))
t3 = Traffic_lamp("(3)", Color.red, random.randint(0, 30))


# changes the status of each lamp
def change_status(tr1, tr2, tr3):
    tr1.color = 1
    tr2.color = 2
    tr3.color = 2
    x1 = random.randint(5, 10)
    x2 = random.randint(0, 5)
    x3 = random.randint(0, 5)
    tr1.cars -= x1
    tr2.cars += x2
    tr3.cars += x3
    print("(1): " + str(tr1.cars) + " Left: " + str(x1))
    print("(2): " + str(tr2.cars) + " came: " + str(x2))
    print("(3): " + str(tr3.cars) + " came: " + str(x3))


print("(1) = lamp_1, (2) = lamp_2, (3) = lamp_3\n"
      " left = the cars that left\n came = the cars that came")
time.sleep(3)

# simulates traffic
while True:
    most_cars = max(t1.cars, t2.cars, t3.cars)
    if most_cars == t1.cars:
        change_status(t1, t2, t3)
    elif most_cars == t2.cars:
        change_status(t2, t1, t3)
    else:
        change_status(t3, t2, t1)
    time.sleep(1.5)
