def F2C (farenheit):
   return round((farenheit - 32) * 5/9, 2)   

tempTable = ["Farenheit | Celcius"]

for i in range(30, 101, 10):
   strOut = str(i) + " | " + str(F2C(i))
   tempTable.append(strOut)

for i in tempTable:
   print(i)
