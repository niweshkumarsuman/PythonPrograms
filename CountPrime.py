def countprime():
    n1=3
    Sum=2
    while(n1<=4000000):
        i=2
        flag=1
        n=n1
        n=int(n**0.5)
        while(i<=n):
            if(n1%i)==0:
                flag=0
                break
            i=i+1
        if flag==1:
            Sum=Sum+n1
        n1=n1+2
    print("Sum=",Sum)
countprime()
        