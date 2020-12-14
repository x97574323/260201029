def rollas(x,y):
  ranger=range(x,y)
  a=list()
  for i in ranger:
    for m in reversed(range(2,i-1)):
      if(i%m==0):
        a.append(i)
        break       
  return(sorted(list(set(ranger)-set(a))))
def main():
  x=int(input("Pls enter:"))
  y=int(input("Pls enter:"))
  print(rollas(x,y))
main()