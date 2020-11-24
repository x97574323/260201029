number=int(input("pls input number:"))
counter=0
matrix_list=list()
traces=list()
while(counter<number):
  local_counter=0
  local=["x"]*number
  while(local_counter<number):
    numof=int(input("pls input element number:"))
    local[local_counter]=numof
    local_counter=local_counter+1
  traces.append(local[counter])
  matrix_list.append(local)
  counter=counter+1
summer=0
for i in matrix_list:
  print(i)
for i in traces:
  summer=summer+i
print("trace of the this matrix:",summer)