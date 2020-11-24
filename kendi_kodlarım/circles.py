#KESİSEN EŞ CEMBERLERİ BULMA 

number_of_circles=int(input("Pls input number of circles:"))
radius=float(input("Pls input the radius of circles:"))
counter=0
coordinates=[]
intersections=list()
while(counter<number_of_circles):
    coordinates_x=float(input("Pls input x coordinate for {}. circle:".format(counter+1)))
    coordinates_y=float(input("Pls input y coordinate for {}. circle:".format(counter+1)))
    coordinates.append([coordinates_x,coordinates_y])
    counter=counter+1
    
for i in coordinates:
    for k in coordinates:
        distance=((i[0]-k[0])**2+(i[1]-k[1])**2)**(1/2)
        if (0<distance<2*(radius)):
            first=coordinates.index(i)
            second=coordinates.index(k)
            if not (([first,second] in intersections) or ([second,first] in intersections) ):
                intersections.append([first,second])
for i in intersections:
    print("{} cemberi ile {} cemberi kesismektedir.".format(i[0]+1,i[1]+1))