
import numpy as np

x=np.random.randint(0,20,(10,10))  
counter=0
print(x)
for i in x:
  counter2=0
  for number in i:
    if(number==15):
      x[counter][counter2]=0
    counter2+=1
  counter+=1

a=100
b=80
c=60
d=40
e=20
rollas=np.array([a,100,b,100,c,100,d,100,e,100])
counter=0
while(counter<10):
  a-=2
  b-=2
  c-=2
  d-=2
  e-=2
  np.append(rollas, [a,100,b,100,c,100,d,100,e,100], axis=0)
  print([a,100,b,100,c,100,d,100,e,100])
  counter+=1
  
def fonksiyon():
  eşleşen=0
  x=list(input("Seq-1:"))
  y=list(input("Seq-2:"))
  for i,t in zip(x,y):
    if(i!=t):
      print("Unpairred position:",posizyon)
      eşleşen+=1
      posizyoner+=1
    else:
      print(posizyoner)
      posizyoner+=1
  print("Score:%",eşleşen*(100/len(x)))
      
  
