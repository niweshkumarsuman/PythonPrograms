def CountNoOfUpperLower():
    x=input("Enter a Sentance:  ")
    l=len(x)
    Sm=0
    Ca=0
    i=0
    while(i<l):
        if x[i].islower():
            Sm=Sm+1
        elif x[i].isupper():
            Ca=Ca+1
        i=i+1
    print("No of Upper Characters: ",Ca)
    print("No of Lower Characters: ",Sm)
CountNoOfUpperLower()
        