num=int(input("enter the number"))
sum = 0
temp = num
while (temp > 0 and temp<=100000):
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if (num == sum):
   print("Armstrong number")
else:
   print("not an Armstrong number")
