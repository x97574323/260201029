number1="1352"
number2="901052"
counter=0
counter1=0
for i in number1:
  if i in number2:
    number2=number2[counter1:]
    counter=counter+1
  counter1=counter1+1
print(counter)