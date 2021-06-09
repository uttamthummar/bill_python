class addressbook:
  def __init__(self,name,contact_no):
    self.name=name
    self.contact_no=contact_no
  def get(self,name,contact_no):
    self.name=name
    self.contact_no=contact_no
  def set(self):
    return self.name,self.contact_no
  def update(self,new_name):
    self.name=new_name
    return self.name
p=addressbook("uttam thummar","9664700156")
print(p.set())
p.get("vijay","1234")
print(p.set())
print(p.update("bhargav"))