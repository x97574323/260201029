number=int(input("Pls input your number:"))

def factorialof(n):
  if (n==0 or n==1):
    return 1
  else:
    return (n*factorialof(n-1))

print(factorialof(number))