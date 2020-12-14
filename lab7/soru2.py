def rollas(x,y):
  ranger=range(x,y)
  a=list()
  for i in ranger:
    if(i%2!=0):
      a.append(i)
  return(a)

def main():
  x=int(input("Pls enter:"))
  y=int(input("Pls enter:"))
  print(rollas(x,y))
main()