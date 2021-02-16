# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:12:32 2020

@author: lenovo
"""
print("Enter the numbers : ")
a,b=input().split(",")
a=int(a)
b=int(b)
print("What you want : +,*,-,/,%,//,** ?" )
c=input()
if(a==45 and b==3 and c=='*'):
    print(555)
elif(a==56 and b==9 and c=='+'):
    print(77)    
elif(a==56 and b==6 and c=='/'):
    print(4)    
elif(c=='+'):
    print("sum of 2 no.'s ",a+b)
elif(c=='-'):
    print("sub of 2 no.'s ",a-b)   
elif(c=='*'):
    print("mul of 2 no.'s ",a*b)    
elif(c=='/'):
    print("div of 2 no.'s ",a/b)
elif(c=='//'):
    print("div of 2 no.'s ",a//b)
elif(c=='%'):
    print("sum of 2 no.'s ",a%b) 
elif(c=='**'):
    print("sum of 2 no.'s ",a**b)    