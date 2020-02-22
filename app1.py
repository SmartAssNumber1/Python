#Ανοίξτε το κείμενο που ονομάζεται test χωρίς την κατάληξη
# get users input
file = input("Enter file's name:")
# open the file
f = open(file + ".txt", mode="r")
WordList = f.read().rsplit(" ")
# default values
NumbersList = [1, 1, 1, 1, 1]
AnswersList = ["Δεν υπάρχει", "Δεν υπάρχει", "Δεν υπάρχει", "Δεν υπάρχει", "Δεν υπάρχει"]
s = 0


# update the list
def update(list_name, list_number, name, position):
    list_number.insert(position, len(name))
    list_name.insert(position, name)
    list_number.pop(5)
    list_name.pop(5)


# search for the 5 longest words
for x in WordList:
    if len(x) >= NumbersList[0]:
        update(AnswersList, NumbersList, x, 0)
        first = len(x)
    elif NumbersList[0] > len(x) >= NumbersList[1]:
        update(AnswersList, NumbersList, x, 1)
        second = len(x)
    elif NumbersList[1] > len(x) >= NumbersList[2]:
        update(AnswersList, NumbersList, x, 2)
        third = len(x)
    elif NumbersList[2] > len(x) >= NumbersList[3]:
        update(AnswersList, NumbersList, x, 3)
        forth = len(x)
    elif NumbersList[3] > len(x) >= NumbersList[4]:
        update(AnswersList, NumbersList, x, 4)
        fifth = len(x)
# invert them without the vowels
for x in AnswersList:
    for y in ['a', 'e', 'i', 'o', 'u']:
        x = x.replace(y, "")
    new_x = x[::-1]
    AnswersList[s] = new_x
    s += 1
# print them
print(AnswersList)
