def sumer(a):
  if(len(a)==1):
    if(a.isinstance()==True):
      return sum(a)
    else:
      return a[0]
  else:
    if(a[-1].isinstance()==True):
      return sum(a[-1])+sumer(a[:-1])
    else:
      return a[-1]+sumer(a[:-1])

print(sumer[1,2,5,[2,5,6]])