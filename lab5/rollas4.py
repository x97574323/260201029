number=int(input("pls input number:"))
counter=0
matrix_list=list()
while(counter<number):
  local_counter=0
  local=["x"]*number
  while(local_counter<number):
    if(local_counter==counter):
      local[local_counter]=1
      local_counter=local_counter+1
    else:
      local[local_counter]=0
      local_counter=local_counter+1
  matrix_list.append(local)
  counter=counter+1
  print(local)
