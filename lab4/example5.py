number=int(input("Pls input your number:"))

def factorialof(n):
  if (n==0 or n==1):
    return 1
  else:
    return (n*factorialof(n-1))

counter=0

num=factorialof(number)
while((num%5==0)):
  counter=counter+1
  num=num//5
print(counter)

