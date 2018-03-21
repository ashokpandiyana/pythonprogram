num1=int(input("enter the number"))
num2=int(input("enter the number"))
factorial = 1
factorial2 = 1
if num1 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num1 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num1 + 1):
       factorial = factorial*i
if num2 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num2 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num2 + 1):
       factorial2 = factorial2*i
print(factorial/factorial2)
