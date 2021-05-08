def List1():
    list2 = ()
    print("Empty List is ",list2)
    list2=(1,2,32,45,"Ramesh Jha")
    length=len(list2)
    print("The no of element :")
    for i in range(length):
        if i==length-1:
            print(list2[length-1])
        else:
            print(list2[i],end=",")
List1()