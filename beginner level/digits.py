 
Num = int(input("Please Enter any Number: "))
Count = 0
while(Num > 0):
    Num = Num // 10
    Count = Count + 1
 
print(" Number of Digits  = %d" %Count)
