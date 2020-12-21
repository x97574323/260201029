email=input("Pls input your email:")
if("@" in email):
  print(checker1)
  if(checker1!="@example.com"):
    print("This is not we are looking for")
  else:
    checker2=email[0:email.index("@")]
    checker3=checker2.lower()
    checker3=checker3.split(".")
    empty=""
    for i in checker3:
      empty=empty+i
    if(empty=="ceng113"):
      print("Welcome")
    else:
      print("Wrong email")
else:
  print("This is not an email!! check your email")