 '''1.Write a program to compute distance between two points taking input from the user (Pythagorean Theorem)'''

import math
print("enter the points : \n ")
x1,y1=input().split(',')
x2,y2=input().split(',')
distance=math.sqrt((int(x2)-int(x1))**2+(int(y2)-int(y1))**2)
print("distance between two points is : ",distance)

''' 2. Write a Program for checking whether the given number is a even number or not. '''

print("enter the number : ")
n=int(input())
if n%2==0:print(n," is even number ")
else:print(n,"is not even")

''' 3.Using a for loop, write a program that prints out the decimal equivalents of 1/2, 1/3, 1/4, . . . 1/10. '''

s=[]
for i in range(2,11):
    s=1/i
    print(s)
 
'''4.Write a program using a while loop that asks the user for a number, and prints a countdown from that number to zero. '''   

print("enter the number")
n=int(input())
while n>=0:
    print(n)
    n=n-1
'''5.Write a program in python that each new term in the Fibonacci sequence is generated by adding the previous two terms. By 
starting with 1 and 2, the first 10 terms will be: 
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... '''

first=0
second=1
for i in range(1,11):
    third=first+second
    print(third)
    first=second
    second=third
 '''6.Write a program to compute the number of characters, words and lines in a file.'''
num_chars=0
num_lines=0
num_words=0
with open("E:\python coding\somya1.txt",'r') as f:
     for line in f:
         words=line.split()
         num_words += len(words)
         num_lines += 1
         num_chars += len(line)
print(words)         
print("no.of characters : ",num_chars)
print("no.of lines",num_lines)   
print("no.of words",num_words)
 
'''7.Write a program in python to find mean, median, mode for the given set of numbers in a list.''' 
 
'''8.Write a program that defines a matrix and prints  '''
a=[][]
for i in range(0,2):
    for j in range(0,2):
        n=a.append(int(input))
'''9.Write a program to perform addition of two square matrices  '''
'''10.Write a program to compute gcd, lcm of two numbers.'''

    