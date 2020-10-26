num1=int(input("Number 1 :"))
num2=int(input("Number 2 :"))
num3=int(input("Number 3 :"))

arrayof=list()
arrayof.append(num1)
arrayof.append(num2)
arrayof.append(num3)

minof=min(arrayof)
print("minimum number is {}".format(minof))