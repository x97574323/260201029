# part 2

number=20
counter=0
while(counter<number):
  local_counter=0
  local=["x"]*number
  while(local_counter<number):
    if(local_counter==counter):
      local[local_counter]=10  
      local_counter=local_counter+1
    else:
      local[local_counter]=2
      local_counter=local_counter+1
  counter=counter+1
  local[-1*counter]=20
  print(local)








# part 3

counter=0
general=[]

while(counter<10):
  matrix1=[4,2,4,2,4,2,4,2,4,2]
  if(counter%2==0):
    general.append(matrix1)
  else:
    general.append(list(reversed(matrix1)))
  counter=counter+1
for i in general:
  print(i)





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

    


