a=int(input("Enter number:"))
temp=a
rev=0
while(a>0 and a<=1000):
    dig=a%10
    rev=rev*10+dig
    a=a//10
if(temp==rev):
    print("This number is a palindrome")
else:
    print("This number isn't a palindrome")
