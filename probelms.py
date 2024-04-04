# write a program to display a persons name,age and address in three different lines 

name='shashank '
age=36
address='INDIA'
print(name)
print (age)
print (address)

#detailed method

name='shashank '
age=36
address='INDIA'
print('name of the person',name)
print ('age of the person',age)
print ('address of the person',address)

# program to swap 2 variable
a= 10
b= 20
a,b=b,a
print('value of a is',a)
print('value of b is',b)

# convert a float into int

a=10.6
print('type of a is ',type(a))
a=(int(a))
print('type of a is',type(a))

# take a detail from students

name=input('enter your name ')
age= input(int('age of student '))
grade=input('enter you grade')
print(name,age,grade)

#create a list of 10 numbers and find out the odd even numbers from it 

# METHOD-1

numbers = [23, 16, 9, 42, 87, 5, 30, 11, 8, 55]
odd_numbers = []
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)  
    else:
        odd_numbers.append(num)  

# Print the results
print("Original list of numbers:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# METHOD-2
N=[1,4,3,6,8,9]
for i in N:
    if i%2 == 0 :
        print(i,"is even number")
    else :
        print(i,'is odd number')

#METHOD-3 (FILTERING METHOD)

N=(1,4,3,6,8,9)
even_numbers =tuple(filter(lambda x: x % 2 == 0, N))
odd_numbers = tuple(filter(lambda x: x % 2 != 0, N))

print("Original list of numbers:", N)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


# FIND THE VOWELS FROM A GIVEN STRING

string= "violet"
vowels=['a','e','i','o','u']

for i in string:
    if i in vowels:
        print(i,'is a vowel')
    else :
        print(i,'is not vowel')
        


arr=[1,23,4,6]
print(arr)

arr.append(200)
arr

arr.insert(2,10)
arr

arr.pop()
arr


arr=[1,2,3,4,56,67,8]
arr.sort()
arr

arr=['shhshjdfdfdhds','sduduyd','kdfbhjd','dhfbdhfdfd']
arr.sort(key=lambda x :len(x) )
arr


# SWAP two numbers

Soltuion:

a=10
b=20

print(a)
print(b)
c=a
a=b

b=c
print(a)
print(b)

another method

a=10
b=20

a,b=b,a

print(a)
print(b)



# checking wheather the number is prime or not 

Soltuion:

list=[1,2,4,8,3,13,99,80]

for i in list:
    if i%2 == 0:
        print (i,"is prime number")
    else :
        print(i,"is not prime number ")

#Write a Python program to reverse a string.

Soltuion:

string='hello world'
reverse=string[::-1]
reverse

#Write a Python program to find the common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = [element for element in list1 if element in list2]
print("Common elements:", common_elements)

# Write a Python program to find the second largest number in a list.
list=[1,22,33,45,67,19,30,3,10]

list.sort()
second_largest_number=list[-2]
second_largest_number



Write a program to find the given number is positive or negative
num = float(input("Enter a number: "))
# Input: 1.2
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

#output: Positive number
   

Write a program to find the sum of two numbers.

num1 = int(input("Enter Number1: "))
# Input1 : 21
num2 = int(input("Enter Number2: "))
#  Input2 : 11
print("sum of given numbers is:", num1 + num2)
#  Output2 : 32 



