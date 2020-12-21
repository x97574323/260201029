def evens(n):
  if(len(n)==1):
    if(n[0]%2==0):
      return 1
    else:
      return 0
  else:
    if(n[-1]%2==0):
      return 1+evens(n[:-1])
    else:
      return evens(n[:-1])
print(evens([1,2,3,4,5]))