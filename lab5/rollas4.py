pas="abc123"
while(True):
  a=input("Enter password:")
  if(a==pas):
    print("Welcome")
    break
  elif(a=="help"):
    print(pas[0])

