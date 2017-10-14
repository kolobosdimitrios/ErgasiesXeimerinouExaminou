passingVehicles = []

for i in range(0,24,1):
    
    print("Insert passing vehicles per 10 minutes... \n")
    x = input()
    int(x)
    passingVehicles.append(x)


print (passingVehicles[0:6] , "\n")
print (passingVehicles[6:12] , "\n")
print (passingVehicles[12:18] , "\n")
print (passingVehicles[18:24] , "\n")


MaxpassingVehPerHour = [max(passingVehicles[0:6]),max(passingVehicles[6:12]),max(passingVehicles[12:18]),max(passingVehicles[18:24])]
stringList = ['4:00pm','5:00pm','6:00pm','7:00pm']

OutputList = []
for x in range (len(stringList)):
    
    OutputList.append((stringList[x],MaxpassingVehPerHour[x]))

print(OutputList)


 
