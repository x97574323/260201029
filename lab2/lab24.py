gpa=float(input("pls input your gpa :"))
number=int(input("pls input your number of lectures:"))

if(gpa<2.0):
  if number<47:
    print("Number of lectures are not enough and gpa is not enough ")
  else:
    print("gpa is not wnough")
else:
  if number<47:
    print("Number of lectures are not enough")
  else:
    print("You can graduate :)")