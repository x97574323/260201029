import time 
def sleeper(n):
  if(n==1):
    time.sleep(1)
    return 1
  else:
    time.sleep(1)
    print(n)
    return sleeper(n-1)    
print(sleeper(5))
