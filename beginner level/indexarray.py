array = []
no = int(input("insert how many elements you want:"))
for i in range(0,no):
    array.append(int(input("Enter next no :")))
for i in range(len(array)):
   print ( i, array[i])
