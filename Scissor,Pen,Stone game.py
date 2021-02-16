''' SCISSOR PAPPER STONE GAME'''
import random
print("GAME START" )
print('S for Scissor')
print(' P for papper')
print('St for Stone')
lst=['Scissor','Papper','Stone']
User_Score= 0
computer_Score= 0
Chances=5
while Chances>=1:
    user_pick=input().capitalize()
    computer_pick= random.choice(lst)
    if user_pick=='S':
        Chances=Chances-1
        if computer_pick=='Scissor':
            print("Draw!")
            #print(f"User_pick{user_pick} and Computer_pick{computer_ pick}")
           # continue
        elif computer_pick=='Papper':
            print("You Won!")
            User_Score += 1
            #print(f"User_pick{user_pick} and Computer_pick{computer_ pick}")
          #  continue
        elif computer_pick=='Stone':
            print("You Loss!")
            computer_Score += 1
           # print(f"User_pick{user_pick} and Computer_pick{computer_ pick}")
           # continue
    elif  user_pick=='P':
        Chances=Chances-1
        if computer_pick=='Papper':
            print("Draw!")
            #print(f"User_pick{user_pick} and Computer_pick{computer_ pick}")
          #  continue
        elif computer_pick=='Scissor':
            print("You Lost!")
            computer_Score += 1
            #print(f"User_pick{user_pick} and Computer_pick{computer_ pick}")
           # continue
        elif computer_pick=='Stone':
            print("You Won!")
            User_Score += 1
            #print(f"User_pick{user_pick} and Computer_pick{computer_ pick}")
          #  continue
    elif user_pick=='St':
        Chances=Chances-1
        if computer_pick=='Stone':
            print("Draw!")
            #print(f"User_pick{user_pick} and Computer_pick{computer_ pick}")
            #continue
        elif computer_pick=='Papper':
            print("You Lost!")
            computer_Score += 1 
            #continue
        elif computer_pick=='Scissor':
            print("You Won!")
            User_Score += 1
            #print(f"User_pick{user_pick} and Computer_pick{computer_ pick}")
            
print("GAME OVER...!!!")
print(f"User_Sore is{User_Score}")
print(f"Computer_Score is {computer_Score}")
if User_Score>computer_Score:
       print("YOU WIN...\n CONGRATS")  
elif User_Score<computer_Score:
       print("YOU LOSS...!!1")  
else:
   print("DRAW..!!!")         