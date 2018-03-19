a=int(input("enter the number"))
b=int(input("enter the number"))
if(a<=100000 and b<=100000):
  a=a+b
  b=a-b
  a=a-b
  print (a)
  print (b)
else:
  print("enter values less than 100000")
