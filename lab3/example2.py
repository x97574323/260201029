year=int(input("Pls input the year:"))

if(year%400==0):
  print("Leap year")
else:
  if(year%4==0):
    if(year%100==0):
      print("İt is not leap year")
    else:
      print("İt is leap year")
  else:
    print("İt is not leap year")

    