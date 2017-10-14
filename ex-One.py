sheepArrayByHour = []

sheepArray = []

night = True

Farmer = True

while (Farmer):

    print ("Grapste tis afixeis ana wra xwrismenes me koma")

    sheepArrayByHour = [int(x) for x in input().split(",")]
       
    sheepArray.append(sheepArrayByHour)
    
    UsInput = input("Telos Metrisewn? \n An nai tote pieste (N) alliws pieste (O): ")    
                        
    if (UsInput == "N"):

        Farmer = False

    elif (UsInput == "O"):

        Farmer = True



print (sheepArray)

totalSheeps = int(input("Grapste posa einai sinolika ta provata: \n"))

Sum = sum(sheepArray[-1])

lost = totalSheeps - Sum

print ("Xathikan:",lost,"provata \n")


        
            
        
        
    
