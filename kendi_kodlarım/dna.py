# part 2
import numpy as ny 

number=20
counter=0
counter2=19


array_gn=ny.full((20,20),2)
while(counter<number):
    array_gn[counter][counter]=10
    array_gn[counter][counter2]=20
    counter=counter+1
    counter2=counter2-1
print((array_gn))





# part 3
import numpy as ny

numberx=10
counterx=0


arrayx=ny.full((10,10),2)
while(counterx<numberx):
    if(counterx%2==0):
        lister=[1,3,5,7,9]
        for i in lister:
            arrayx[counterx][lister]=4
    else:
        lister2=[0,2,4,6,8]
        for i in lister2:
            arrayx[counterx][i]=4
    counterx=counterx+1
print(arrayx) 




# part 1


reference="atgtctgattta"
patient1="atgtctgattta"
patient2="atgtctgattta"
patient3="atctctgattta"
patient4="atgtctgattta"
patient5="atgtctgattta"
patient6="atgtctgattta"
patient7="atctctgattta"
patient8="atgtctgattta"
patient9="atctctgattta"
patient10="atgtctgattta"
lister=[patient1,patient2,patient3,patient4,patient5,patient6,patient7,patient8,patient9,patient10]
counter=0

for i in lister:
    if(reference==i):
        globals()["{}".format(counter)] =["patient",counter,"No canser risk"]
        print(globals()["{}".format(counter)])
        counter=counter+1
    else:
      
        globals()["{}".format(counter)] =["patient",counter,"Canser risk"]
        print(globals()["{}".format(counter)])
        counter=counter+1

    
    

