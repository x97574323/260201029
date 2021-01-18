def rollas(a):

  if(a==1):
    return 3
  else:
    return 3+rollas(a-1)

print(rollas(6))