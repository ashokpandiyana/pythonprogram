x=input("enter the number")
a,b=x.split(" ")
a=int(a)
b=int(b)
if(a>0 and  a<=10000):
  if(b>0 and  b<=10000):
    for i in range(1,20):
        if(a%i==0 and b%i==0):
          print(i)
          
      
