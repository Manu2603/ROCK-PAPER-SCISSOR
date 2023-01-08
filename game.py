H_score=0 #global variable
C_score=0
Tie=0
def getHuman_In():
  #rock paper sciccor
  H_in=input("Enter your input :")
  H_in=H_in.lower()
  if  H_in=='r' or H_in=='p' or H_in=='s' :
    print("Your input :",H_in)
    return H_in
  else:
    print("Wrong input!!!.....\nEnter again ->")
    getHuman_In()
####
def generateComputer_In():
  C_in = ""
  n=random.randint(0,3)  #randint(x,y+1)
  if n==0:
    C_in='r'
  elif n==1:
    C_in='p'
  else :
    C_in='s'
  print("Computer input :",C_in)
  return C_in
####
def compare(H_in,C_in) :
  global H_score 
  global C_score 
  global Tie 
  human_In=H_in
  computer_In=C_in
  if human_In == computer_In :
     Tie+=1
  elif human_In=='r' and computer_In=='p':
    print ("Computer Wins🎉....")
    C_score+=1
  elif human_In=='p' and computer_In=='s':
    print ("Computer Wins🎉....")
    C_score+=1
  elif human_In=='s' and computer_In=='r':
    print ("Computer Wins🎉....")
    C_score+=1
  elif human_In=='r' and computer_In=='s':
    print ("You Win🎉....")
    H_score+=1
  elif human_In=='s' and computer_In=='p':
    print ("You Win🎉....")
    H_score+=1
  elif human_In=='p' and computer_In=='r':
    print ("You Win🎉....")
    H_score+=1
  print("Score Board :\n You->{}  Computer->{}  Tie->{}".format(H_score,C_score,Tie))
###
def winner(H_score,C_score,Tie):
  if H_score > C_score :
    print("Congrates You Won🎉🎊......")
  elif C_score > H_score :
    print("Oops....You Lost")
  else:
    print("Score Tie...")
  
 
####
def ask():
  ch=input("Want to play again (Y/N) :")
  ch.upper()
  return ch 
####
def reset():
  global H_score
  H_score=0
  global C_score
  C_score=0
  global Tie
  Tie=0
#combined
import random
playagain=" "
while playagain!='n':
    print("Rock||Paper||Sissor")
    H = getHuman_In()  
    C = generateComputer_In()
    compare(H,C)
    playagain=ask()
winner(H_score,C_score,Tie)
reset()
print("Thanks see you again🙂...")
