a=[]
b=[]
c=[]
no1=int(input("enter the number"))
no2=int(input("enter the number"))
for x in range(no1):
  a.append(int(input("enter the number in 1")))
for z in range(no2):
  b.append(int(input("enter the number in 2")))
c=b[ ::-1]
if(a==c):
  print("yes")
else:
  print("no")
