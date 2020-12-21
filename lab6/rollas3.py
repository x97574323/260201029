list_input=input("Pls input your numbers:").split(",")
if(len(list_input[0])>1):
  list_input[0]=list_input[0][-1]
if(len(list_input[-1])>1):
  list_input[-1]=list_input[-1][0]
converted_list=[]
for i in list_input:
    converted_list.append(int(i))
setter=set(converted_list)
rollas=list()
for k in setter:
    rollas.append(k)
rollas=sorted(rollas)
rollas=reversed(rollas)
print("your list:",list(rollas))
