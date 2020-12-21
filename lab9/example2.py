def get_reversed(n):
  if(len(n)==1):
    return n
  else:
    return (([n[-1]])+(get_reversed(n[:-1])))
print(get_reversed([1,2,3,4,5]))