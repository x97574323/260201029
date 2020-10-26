age=int(input("input your age:"))

if age<6 or age>60:
  print("Free ticket")
else:
  if 6<age<18:
    print("%50 discount 1.5 TL")
  else:
    print("ticket is 3 TL")