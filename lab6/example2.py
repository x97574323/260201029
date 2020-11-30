books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
empty=dict()
for i in books:
  a=len(i)
  b=(len(set(list(i))))
  empty[i]=(a,b)
print(empty)