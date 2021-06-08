catagory_arr=["electrical","cosmetic","grocery"]
person=[]

def catagory():
  global catagory_arr
  for i in range(0,len(catagory_arr)):
    print("press",i,"for" ,catagory_arr[i])
  choice=int(input("enter catagory of items:"))
  items(choice)

def items(c):
  for key in catagory_arr:
    electrical={"fan": 500,"light": 200 }
    cosmetic={"powder":200,"shampoo":50}
    grocery={"wheat":500,"rise":400 }
    if catagory_arr[c]==key:
      if key=="electrical":
        for index,(key, value) in enumerate(electrical.items()):
          print ("press",index+1,"for",key, "at", value)
        select_item(**electrical)     
      elif key=="cosmetic":
        for index,(key, value) in enumerate(cosmetic.items()):
          print ("press",index+1,"for",key, "at", value)
        select_item(**cosmetic)
      elif key=="grocery":
        for index,(key, value) in enumerate(grocery.items()):
          print ("press",index+1,"for",key, "at", value)
        select_item(**grocery)
      else:
        print("wrong choice")
  return key

def select_item(**c):
  choice1=int(input("enter catagory of items :"))
  quantity=int(input("enter quantity of items:"))
  my_list=list(c)
  p_name=my_list[choice1-1]
  p_price=c.get(p_name)
  total=quantity*p_price
  single_pr=[p_name,p_price,quantity,total]
  person.append(single_pr)
  print(person)
  options()

def options():
  add=int(input("press 1 for add anything! 2 for edit 3 for check out"))
  if(add==1):
    c=catagory()
  if(add==2):
    edit()
  elif(add==3):
    print_list()

def print_list():
  print("------------------------------------")
  print("sr_no\tp_name\tp_price\tquantity")
  print("------------------------------------")
  for i in range(0,len(person)):
    print(i+1,"\t",person[i][0],"\t",person[i][1],"\t",person[i][2],"\t",person[i][3] )
    print("----------------------------------")
    total_bill_am()

def edit():
  print_list()
  c1=int(input("1 for changing and 2 for delete"))
  sr_no=int(input("enter sr no:"))
  if (c1==1):
    single_pr=person[sr_no-1]
    quantity=int(input("enter quantity of items:"))
    total=quantity*person[sr_no-1][1]
    single_pr=person[sr_no-1]
    single_pr[2]=quantity
    single_pr[3]=total
    print_list()
    options()
    
  elif(c1==2):
    person.pop(sr_no-1)
    print_list()
    options()
    
  else:
    print("not valid")

def total_bill_am():
  total_bill=0
  for i in range(0,len(person)):
    total_bill +=person[i][3]
  print("total_bill:",total_bill)
c=catagory()