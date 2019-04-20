import random
tenRandom = random.sample(range(0, 100), 10)
print ("Every element: ", tenRandom)
print ("Even Index: ", tenRandom[0::2])
myList = list()
for i in tenRandom:
    if i % 2 == 0:   
        myList.append(i)
print("Every even: ", myList)
reverseList = list(reversed(tenRandom)) #non-destructive
print("Reverse Order: ", reverseList)
firstAndLast = [tenRandom[0], tenRandom[-1]]
print("First and Last: ", firstAndLast)
