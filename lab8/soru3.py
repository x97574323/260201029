import random
def get_rand_list(x,y,n):
  counter=n
  array2=list()
  array1=list()
  while(counter>0):
    number=random.randint(x,y)
    array2.append(number)
    counter-=1
  counter=n
  while(counter>0):
    number=random.randint(x,y)
    array1.append(number)
    counter-=1
  return (array2,array1)
def get_overlap(a,b):
  return list(set(a) & set(b))
def main():
  x=1
  y=15
  n=7
  rollas=get_rand_list(x,y,n)
  print(get_overlap(rollas[0],rollas[1]))
main()