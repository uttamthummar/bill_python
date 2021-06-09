class bank():
  def __init__(self,name):
    self.name=name
    self.balance=0
    print("hello {}".format(self.name))
    print("account balance {}".format(self.balance))
  def deposite(self):
    deposite=int(input("enter amount for deposite"))
    self.balance +=deposite
    print("total balance:",self.balance)
    print("debited amount:",deposite)
  def withdrow(self):
    withdrow=int(input("enter amount te withdrow"))
    if (self.balance>withdrow):
      self.balance -=withdrow
      print("total balance:",self.balance)
      print("credited amount:",withdrow) 
    else:
      print("balance not available")    

choice=int(input("1 for new account 2 for deposite 3 for credit 4 for exit"))
while(choice!=4):
  if(choice==1):
    name1=str(input("enter your name"))
    p=bank(name1)
  elif(choice==2):
    p.deposite()
  elif(choice==3):
    p.withdrow()
  else:
    print("enter valid choice")
  choice=int(input("1 for new account 2 for deposite 3 for credit 4 for exit"))
