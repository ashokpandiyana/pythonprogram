a=int(input("enter the number"))
if(a>1 and a<=1000):
  for i in range(2,a):
    if(a%i==0):
      print("it is not a prime number")
      break
  else:
    print("prime number")
