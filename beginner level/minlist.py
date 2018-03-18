array = []
no = int(input("insert how many elements you want:"))
for i in range(0,no):
    array.append(int(input("Enter next no :")))
if(array[-1]<=100000):
  print (min(array))
