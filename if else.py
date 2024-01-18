a=8
if a>9:
    print('We started to work on conditional statements')
    print("The condition is true")
print("hi")  
# output will be "hi" bcz condition not satisfied


x=5
if x==6:# If condition is false
    print('The if condition is true')
else:
    print('Else condition got executed')


x=11
if(x==10):
    print('i am in if block')
elif(x==11):   
# elif will help in checking more than 1 if condition
    print('i am in elif block')
elif(x==0):
    print('Zero number')
else:
    print('i am in else block')  



 x = int(input('enter the number: '))

if x>0:
    print("X is positive")
elif x<0:
    print("X is Negative")
    print('i am in elif block')
else:
    print("X is Zero")
    print('i am in else block')

print('outside of the loop') 

import datetime
from datetime import date

today=date.today()

today.isoweekday()