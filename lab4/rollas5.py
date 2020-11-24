def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return (recur_fibo(n-1) + recur_fibo(n-2))

number=int(input("Pls input:"))

while(number>0):
    print(recur_fibo(number),end=" ")
    number=number-1






