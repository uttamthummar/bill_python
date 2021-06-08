n=int(input("enter length of list"))
a=[]
for i in range(0,n):
  ele=int(input("enter value:"))
  a.append(ele)

c=int(input("enter div:"))
inc = 1
while len(a) > 1: 
  for i in range(1,len(a)):
    if c == inc:
      del a[0]
      inc = 1
      print(a)      
    else:
      b=a[0]
      del a[0]
      inc += 1;
      a.append(b)

