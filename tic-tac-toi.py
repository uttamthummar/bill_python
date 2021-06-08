winner=1
currunt_player="O"
def print_box():
  for i in range(len(box)):
    for j in range(len(box[i])):
      print(box[i][j],end=" ")
    print()

def player_choice():
  k=0
  choice_row=int(input("enter positions of row"))
  choice_col=int(input("enter positions of col"))
  global currunt_player
  if(i%2==0):
    box[choice_row][choice_col]="O"
    print_box()
  else:
    box[choice_row][choice_col]="X"
    print_box()


def win():
  global winner
  if((box[0][0]=="O" and box[0][1]=="O" and box[0][2]=="O") or (box[1][0]=="O" and box[1][1]=="O" and box[1][2]=="O") or 
  (box[2][0]=="O" and box[2][1]=="O" and box[2][2]=="O") or (box[0][0]=="O" and box[1][0]=="O" and box[2][0]=="O") or
  (box[0][1]=="O" and box[1][1]=="O" and box[2][1]=="O") or (box[0][2]=="O" and box[1][2]=="O" and box[2][2]=="O") or 
  (box[0][0]=="O" and box[1][1]=="O" and box[2][2]=="O") or (box[0][2]=="O" and box[1][1]=="O" and box[2][0]=="O")) :
    print("player one win")
    winner=0
  elif((box[0][0]=="X" and box[0][1]=="X" and box[0][2]=="X") or (box[1][0]=="X" and box[1][1]=="X" and box[1][2]=="X") or 
  (box[2][0]=="X" and box[2][1]=="X" and box[2][2]=="X") or (box[0][0]=="X" and box[1][0]=="X" and box[2][0]=="X") or
  (box[0][1]=="X" and box[1][1]=="X" and box[2][1]=="X") or (box[0][2]=="X" and box[1][2]=="X" and box[2][2]=="X") or 
  (box[0][0]=="X" and box[1][1]=="X" and box[2][2]=="X") or (box[0][2]=="X" and box[1][1]=="X" and box[2][0]=="X")) :
    print("player two win")
    winner=0

row,cols=3,3
i=0
k=1
box=[[1 for i in range(cols)] for j in range(row)] 
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

