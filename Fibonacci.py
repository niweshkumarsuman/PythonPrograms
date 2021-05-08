a=0
b=1

num=int(input("Enter the vale of n for fibonaci "))
print("The Fibonaci series ",num)
print(a , b , end=" ")
i=3
while(i<=num):
    s=a+b
    a=b
    b=s
    print(s, end=" ")
    i=i+1

    
    