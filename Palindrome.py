#to check palindrome
num=input("Enter a Number\n")
rev=num[: : -1]
if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")