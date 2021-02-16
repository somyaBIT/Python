# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:24:01 2020

@author: lenovo
"""

import random
winning_no=random.randint(1,100)
for i in range(5):
    print("guess the no. between 1-100")
    a=int(input())
    if(a==winning_no):
        print(f"Congrats,You Win...!!at guess : {i+1}")
    elif(a>winning_no):
         print(f"Too High \n guess left : {5-(i+1)}")
    elif(a<winning_no):
       print(f"Too Low \n guess left : {5-(i+1)}")
print("Game Over..!!!")
print("Winning Number is ",winning_no)
print("Sorry,you lose..!!\n Better luck next time" )   