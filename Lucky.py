Lucky,Num=map(int,input("Enter a Number: ").split())
Sum=0
Org=Num
while(Num!=0 or Sum>9):
    if Num==0:
        Num=Sum
        Sum=0
    rem=(Num%10)
    Sum=Sum+rem
    Num=(Num//10)
if Lucky==Sum:
    Lucky=Lucky+9
print("Suggested Number is {}".format(Org+abs(Lucky-Sum)))
