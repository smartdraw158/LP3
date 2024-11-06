n=int (input("How many trems?"))
a,b=0,1
count=0

if n<=0:
    print("please enter positive enteger!!")
elif n==1:
    print("fibonaci series upto",n,":")
    print(a)
else:
    print("fibonaci series: ")
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
        