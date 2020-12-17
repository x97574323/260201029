file=open("provinces.txt","r")
data=file.readlines()
file.close()
data=[m.strip("\n") for m in data]
array=[i.split(",") for i in data]
nearest=[]
while(True):
    closest1=[]
    city1=input("Departure province:\n").upper()
    booler1=False
    for i in array:
        if(i[0]==city1):
            x1=float(i[1])
            y1=float(i[2])
            booler1=True
            break
        elif(i[0].startswith(city1)):
            closest1.append(i[0])
    if(booler1==True):
        for t in array:
            distancer=(((x1-float(t[1]))**2+(y1-float(t[2]))**2)**(1/2))*100
            nearest.append([distancer,t[0]])
        break
    else:
        closest1=sorted(closest1)
        print("Province not found!")
        if(2>len(closest1)>0):
            print("Possible province:",end ="")
            print(*closest1,sep=',')
        if(len(closest1)>1):
            print("Possible provinces:",end ="")
            print(*closest1,sep=',')
nearest=sorted(nearest)
while(True):
    closest2=[]
    city2=input("Arrival province:\n").upper()
    if(city2!=city1):
        booler2=False
        for i in array:
            if(i[0]==city2):
                x2=float(i[1])
                y2=float(i[2])
                booler2=True
                break
            elif(i[0].startswith(city2)):
                closest2.append(i[0])
        if(booler2==True):
            break
        else:
            closest2=sorted(closest2)
            print("Province not found!")
            if(2>len(closest2)>0):
                print("Possible province:",end ="")
                print(*closest2,sep=',')
            elif(len(closest2)>1):
                print("Possible provinces:",end ="")
                print(*closest2,sep=',')
    else:
        print("Enter a different province!")
distance=(((x1-x2)**2+(y1-y2)**2)**(1/2))*100
while(True):
    vehicle=input("Enter travel type:\n").upper()
    if(vehicle=="CAR"):
        time=distance/90
        hours=int(time)
        minutes=int((time-hours)*60)
        break
    elif(vehicle=="MOTORCYCLE"):
        time=distance/60
        hours=int(time)
        minutes=int((time-hours)*60)
        break
    elif(vehicle=="BICYCLE"):
        time=distance/25
        hours=int(time)
        minutes=int((time-hours)*60)
        break

rollas=sorted([nearest[1][1],nearest[2][1],nearest[3][1]])
print("\nI am calculating the distance between",city1,"and",city2,"...")
print("\nDistance:",round(distance,2),"km")
print("Approximate travel time with",vehicle+":", hours,"hours",minutes ,"minutes")
print("Recommended places close to",city1+":"+rollas[0]+","+rollas[1]+","+rollas[2])