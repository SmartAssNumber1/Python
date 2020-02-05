# declare the default values
dictionary = {}
value = 0
# get users input
tax = input("Enter tax percentage:")
# check if the user has ended with the char %
if tax[-1] == '%':
    tax = tax[:-1]
while True:
    item = input("Enter item:")
    if item == "end":
        break
    price = input("Enter the price:")
    if price[-1] == '$':
        price = price[:-1]
    # adds the items to the dictionary
    dictionary[item] = int(price)
    # sums the values and applies the tax modifier
for x in dictionary:
    value += dictionary[x]
print("Your total sum is: " + str(value*(int(tax)/100) + value))
