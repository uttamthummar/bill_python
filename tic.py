winner=1
def print_box():
  global box
  m=1
  for i in range (1,10):
    box.append(i)
  for i in range(1,10):
    print(box[i],end=" ")
    while m==3:
      print("\n")
      m=0
    m+=1
  
def player_choice():
  global i,k
  position=int(input("enter position for sign:"))
  if(box[position]==1):
    if(i%2==0):
      box[position]="O"
      print_box()
    else:
      box[position]="X"
      print_box()
  else:
    print("enter valid choice")
    i-=1
    k-=1

def win():
  global winner
  if((box[1]=="O" and box[2]=="O" and box[3]=="O") or (box[4]=="O" and box[5]=="O" and box[6]=="O") or 
  (box[7]=="O" and box[8]=="O" and box[9]=="O") or (box[1]=="O" and box[4]=="O" and box[7]=="O") or
  (box[2]=="O" and box[5]=="O" and box[8]=="O") or (box[3]=="O" and box[6]=="O" and box[9]=="O") or 
  (box[1]=="O" and box[5]=="O" and box[9]=="O") or (box[3]=="O" and box[5]=="O" and box[7]=="O")) :
    print("player one win")
    winner=0
  elif((box[1]=="O" and box[2]=="O" and box[3]=="O") or (box[4]=="O" and box[5]=="O" and box[6]=="O") or 
  (box[7]=="O" and box[8]=="O" and box[9]=="O") or (box[1]=="O" and box[4]=="O" and box[7]=="O") or
  (box[2]=="O" and box[5]=="O" and box[8]=="O") or (box[3]=="O" and box[6]=="O" and box[9]=="O") or 
  (box[1]=="O" and box[5]=="O" and box[9]=="O") or (box[3]=="O" and box[5]=="O" and box[7]=="O")) :
    print("player two win")
    winner=0

box=[1,1,1,1,1,1,1,1,1]
i=0
k=1 
print_box()
while(i<9 and winner!=0):
  if(k%2==0):
    print("player two choice")
  else:
    print("player one choices")
  player_choice()
  win()
  i+=1
  k+=1
  if winner==0:
    break
  if i==9 and winner!=0:
    print("draw")