num=int(input("enter the number"))
factorial = 1
if (num<0):
   print("no factorial")
elif num == 0:
   print("1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of is ",factorial)
