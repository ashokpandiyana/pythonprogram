array = []
no = int(input("insert how many elements you want:"))
if(no<=100000 and no>=1):
  for i in range(0,no):
    array.append(int(input("Enter next no :")))
  print (min(array))
