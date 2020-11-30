members=[("Jon",15),("Ned",45),("Arya",9),("catelyn",44),("Bran",10)]
mem=dict()
for i in members:
  mem[i[0]]=i[1]
for i in mem:
  if(mem[i]<18):
    print(i)