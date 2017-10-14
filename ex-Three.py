import urllib2
import json

#Epistrefei True gia swsti eisodo kai false gia lathos eisodo
def isCity(city_,List):

    Flag = False

    for val in List:
        if (val['name'] == city_):
            Flag = True



    return Flag
        
            
    
    
#Epistrefei ta score tis kathe polis
def takeTheCitiesScores(link):

    response = urllib2.urlopen(link)

    List = json.load(response)

    List = List['categories']

    

    return List




#Pernei oles tis poleis apo to teleport
def takeThecitiesNames():

    response = urllib2.urlopen("https://api.teleport.org/api/urban_areas/")

    AllCityList = json.load(response)
    AllCityList = AllCityList['_links'].get('ua:item')
    
    

    return AllCityList


#psaxnei na vrei tin poli pou edwse o xrisris
##an den yparxei typwnei lathos eisodos alliws pigainei
### ( https://api.teleport.org/api/urban_areas/slug:$city$/scores/ )
def searchTheInputList(city_,List):

        for val in List:
            
            if (val['name'] == city_) :
                url = val['href']

        return Responses(url)  

        
#Pernei ta responses apo ton server    
def Responses(String):

    Response = urllib2.urlopen(String)
    Response = json.load(Response)
    
    return Response




#Eisodos twn polewn apo ton xristi
firstCity = raw_input("Prwti poli : ")
print '\n'
secondCity = raw_input("Defteri poli : ")
print '\n'
cityNamesList = takeThecitiesNames()
Input_1 = isCity(firstCity,cityNamesList)
Input_2 = isCity(secondCity,cityNamesList)
if (Input_1 and Input_2):
    responseList1 = searchTheInputList(firstCity,cityNamesList)
    responseList2 = searchTheInputList(secondCity,cityNamesList)
    url1 = responseList1['_links'].get('ua:scores')
    url1 = url1['href']
    url2 = responseList2['_links'].get('ua:scores')
    url2 = url2['href']
    Scores1 = takeTheCitiesScores(url1)
    Scores2 = takeTheCitiesScores(url2)
    ScoresList1 = []
    ScoresList2 = []
    for val in Scores1:
        ScoresList1.append(val['score_out_of_10'])


    for val in Scores2:
        ScoresList2.append(val['score_out_of_10'])

    count_1 = count_2 = 0    
    for row in range(len(ScoresList1)):
        if ( ScoresList1[row] > ScoresList2[row] ):
            count_1 = count_1 + 1
        elif( ScoresList1[row] < ScoresList2[row] ):
            count_2 = count_2 + 1

    if (count_1 == count_2):
        print 'Kammia den iperixe tis allis'
    elif(count_1  > count_2):
        print 'H poli : ',firstCity,' iperixe tis polis : ',secondCity,' kata : ' ,count_1,'\n'
    else:
        print 'H poli : ',secondCity,' iperixe tis polis : ',firstCity,' kata : ',count_2,'\n'


else:
    print '\n'
    print "WRONG INSERT"    

    



    


