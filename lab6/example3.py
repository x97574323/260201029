books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
empty=dict()
for i in books:
  a=len(i)
  b=(len(set((i))))
  empty[i]=(a,b,(a+b)/2)
print(empty)
