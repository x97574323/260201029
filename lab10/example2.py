def heil_hitler(m):
  if(m==1):
    return "m"
  else:
    if(m%2==0):
      return [m]+heil_hitler(m//2)
    else:
      return [m]+heil_hitler(3*m-1)

print(heil_hitler(5))