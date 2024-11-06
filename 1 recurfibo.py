def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
    

n=int (input("How many trems?"))
if n<=0:
    print("please enter a positive integer!!")
else:
    print("fibonacci series:")
    for i in range(n):
        print(recur_fibo(i))
