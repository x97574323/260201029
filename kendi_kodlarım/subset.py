import math
import random 
all_items=[5,7,9,8]
subsets=[]
counter=1
while counter<len(all_items)+1:
    local=[]
    while(True):
        number_of_items=math.factorial(len(all_items))/(math.factorial(len(all_items)-counter)*math.factorial(counter))
        elements=random.sample(all_items,counter)
        if(len(local)==number_of_items):
            break 
        else:
            elements=sorted(elements)
            if ( not (elements in local)):
                local.append(elements)
    counter=counter+1
    for i in local:
        subsets.append(i)
subsets.append([])
print(subsets)
print("length of subsets for {} element:".format(len(all_items)),len(subsets))
