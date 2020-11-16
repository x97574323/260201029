number=int(input("Pls input your number:"))
number1=number
even=list()
while(number1>0):
  numof=int(input("pls input number:"))
  if(numof%2==0):
    even.append(numof)
  number1=number1-1
print((len(even)/number)*100)
